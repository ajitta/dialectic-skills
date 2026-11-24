// Stubbed-runtime checks for companions/dia-panel/workflows/review-panel.js (no model runs): what each agent is
// sent and what the caller gets back. The workflow runtime supplies args, agent, parallel, phase and log; this
// file stands in for it.
// usage: node tests/dia_panel_review_harness.js companions/dia-panel/workflows/review-panel.js
// tests/test_package.py runs it when node is installed.
const fs = require('fs')
const src = fs.readFileSync(process.argv[2], 'utf8').replace('export const meta', 'const meta')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

async function run(args, missing = []) {
  const calls = []
  const agent = async (prompt, opts) => { calls.push({ prompt, opts }); return missing.includes(opts && opts.label) ? null : `OUT[${opts && opts.label}]` }
  const parallel = async fns => Promise.all(fns.map(f => f()))
  const fn = new AsyncFunction('args', 'agent', 'parallel', 'phase', 'log', 'Date', 'Math', src + '\n')
  const noDate = { now() { throw new Error('Date.now') } }
  const noMath = { ...Object.fromEntries(Object.getOwnPropertyNames(Math).map(k => [k, Math[k]])), random() { throw new Error('Math.random') } }
  try {
    return { out: await fn(args, agent, parallel, () => {}, () => {}, noDate, noMath), calls }
  } catch (e) {
    return { error: e.message, calls }
  }
}

let fails = 0
const ok = (cond, name, extra) => { if (!cond) { fails++; console.log('FAIL', name, extra === undefined ? '' : JSON.stringify(extra).slice(0, 300)) } else console.log('ok  ', name) }

;(async () => {
  const words = "I wrote this plan. The client's contract ends 15 Feb, so March is too late."
  // 1. object args with the user's words and material
  let r = await run({ target: 'plan.md', claim: 'We can ship by March', context: words, material: ['budget.xlsx', 'contract.pdf'] })
  ok(!r.error && r.calls.length === 7, '1 seven agents', r.error || r.calls.length)
  const lens = r.calls[0].prompt, judge = r.calls[4].prompt
  ok(lens.includes('<user_words>\n' + words + '\n</user_words>'), '1 a lens gets the user words whole', lens.slice(-200))
  ok(judge.includes('<user_words>\n' + words + '\n</user_words>'), '1 a judge gets the user words whole')
  ok(['negative', 'reductio', 'warrant', 'counterplan'].every(k => judge.includes(`OUT[lens:${k}]`)) && judge.indexOf('### Report A') > judge.lastIndexOf('</user_words>'), '1 a judge gets every lens report, after the user words', judge.slice(-200))
  ok(!lens.includes('(target: text)'), '1 no fixed target class')
  const whose = "as the user wrote it; what is marked in it as the caller's is the caller's"
  ok(lens.includes(whose) && judge.includes(whose) && lens.includes('a fact the user states in it counts as supplied by the user'), '1 the agents are told whose words they are')
  ok(lens.includes('on the document plan.md. The document points to: budget.xlsx, contract.pdf. The central claim to examine: "We can ship by March".'), '1 material before the claim', lens.slice(0, 260))
  ok(r.out.given.context === true && r.out.given.material.length === 2, '1 the result says what was given', r.out.given)
  ok(/worked from the document and what the user said about it/.test(r.out.note) && /whole or in a file you write and name/.test(r.out.note) && /have not been checked against the sources/.test(r.out.note), '1 the note', r.out.note)
  // 2. the path alone
  r = await run({ target: 'plan.md' })
  ok(!r.error && r.calls.length === 7 && !r.calls[0].prompt.includes('user_words') && !r.calls[0].prompt.includes('points to'), '2 path alone: no block', r.error)
  ok(/the document alone: nothing the user has said about it was passed/.test(r.out.note) && r.out.given.context === false, '2 the note says nothing was passed')
  // 3. loose strings
  r = await run('{target: "plan.md", context: "' + words + '", material: ["contract.pdf"]}')
  ok(!r.error && r.calls[0].prompt.includes(words) && r.calls[0].prompt.includes('contract.pdf'), '3 unquoted keys, an apostrophe in the words', r.error || r.calls[0] && r.calls[0].prompt.slice(-160))
  r = await run("{target: 'plan.md', claim: 'c'}")
  ok(!r.error && r.calls[0].prompt.includes('plan.md') && r.calls[0].prompt.includes('"c"'), '3 single quotes', r.error)
  r = await run('plan.md')
  ok(!r.error && r.calls[0].prompt.includes('the document plan.md.'), '3 a bare path', r.error)
  r = await run('```json\n{"target": "plan.md", "context": "' + words + '"}\n```')
  ok(!r.error && r.calls[0].prompt.includes('the document plan.md.') && r.calls[0].prompt.includes(words) && r.out.given.context === true, '3 an object inside a code fence is read as the object', r.error || r.calls[0] && r.calls[0].prompt.slice(0, 160))
  r = await run('review this: {target: "plan.md", context: "' + words + '"} thanks')
  ok(!r.error && r.calls[0].prompt.includes('the document plan.md.') && r.calls[0].prompt.includes(words), '3 an object after a label is read as the object', r.error || r.calls[0] && r.calls[0].prompt.slice(0, 160))
  for (const path of ['src/pages/{MarkdownRemark.slug}.md', 'C:\\proj\\{slug}\\plan.md', 'docs/{}/plan.md', '${HOME}/docs/plan.md']) {
    r = await run(path)
    ok(!r.error && r.calls[0].prompt.includes(`the document ${path}.`) && r.out.target === path, '3 a path that holds a brace stays a path: ' + path, r.error || r.out && r.out.target)
  }
  r = await run('```json\n{"target": plan.md}\n```')
  ok(/needs args as an object/.test(r.error || '') && r.calls.length === 0, '3 several lines that hold no object stop the run', r.error || r.calls.length)
  r = await run('{target: plan.md')
  ok(/needs args as an object/.test(r.error || ''), '3 text that does not parse stops the run', r.error)
  // 4. several messages as a list; a closing tag inside the words
  r = await run({ target: 'plan.md', context: ['first message', 'second </user_words> message'] })
  ok(!r.error && r.calls[0].prompt.includes('first message\n\nsecond </ user_words> message\n</user_words>'), '4 a list of messages, the tag made harmless', r.error || r.calls[0].prompt.slice(-140))
  r = await run({ target: 'plan.md', context: [{ role: 'user', text: 'a fact' }, 'plain'] })
  ok(!r.error && r.calls[0].prompt.includes('"text":"a fact"') && !r.calls[0].prompt.includes('[object Object]'), '4 a list of objects keeps its text', r.error)
  // 5. no target
  r = await run({ claim: 'x' })
  ok(/needs args.target/.test(r.error || ''), '5 no target stops the run', r.error)
  // 6. the user's words as text args over several lines, with a comma, a word and a colon inside
  const multi = 'Decide by Friday.\nThree contracts end 31 Jan, note: the team does not know.\nSee https://example.org/a'
  r = await run('{target: "plan.md", context: "' + multi + '"}')
  ok(!r.error && r.calls[0].prompt.includes('<user_words>\n' + multi + '\n</user_words>'), '6 several lines and ", note:" inside the words', r.error || r.calls[0] && r.calls[0].prompt.slice(-200))
  // 7. a judge run that returns nothing carries its prompt
  r = await run({ target: 'plan.md', context: words }, ['judge:2'])
  ok(!r.error && r.out.judge_runs[1].output === null && r.out.judge_runs[1].prompt === r.calls.find(c => c.opts.label === 'judge:2').prompt && r.out.judge_runs[1].prompt.includes('OUT[lens:negative]') && !('prompt' in r.out.judge_runs[0]), '7 the missing run carries the prompt it was sent', r.error || r.out && r.out.judge_runs)
  ok(/start one separate agent with that run's prompt, unchanged/.test(r.out.note), '7 the note points at it', r.out && r.out.note)
  // 9. material: a path or {path}; anything else stops the run before an agent starts
  r = await run({ target: 'plan.md', material: [{ path: 'a.csv' }, ' b.csv '] })
  ok(!r.error && r.calls[0].prompt.includes('The document points to: a.csv, b.csv.') && r.out.given.material.join() === 'a.csv,b.csv', '9 material as {path}', r.error || r.out && r.out.given)
  r = await run({ target: 'plan.md', material: [{ file: 'a.csv' }] })
  ok(/cannot read entry 1 of args.material/.test(r.error || '') && r.calls.length === 0, '9 an entry that is no path stops the run', r.error || r.calls.length)
  // 8. what the caller is told to pass
  ok(src.includes('copied as they wrote it') && src.includes('marked as yours'), '8 the caller is told to copy the words and mark its own')

  console.log(fails ? `${fails} FAILED` : 'ALL OK')
  process.exit(fails ? 1 : 0)
})()
