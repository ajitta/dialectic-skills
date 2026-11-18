// Stubbed-runtime checks for companions/dia-panel/workflows/judge.js (no model runs).
// The workflow runtime supplies args, agent, parallel, phase and log; this file stands in for it.
// usage: node tests/dia_panel_judge_harness.js companions/dia-panel/workflows/judge.js
// tests/test_package.py runs it when node is installed.
const fs = require('fs')
const src = fs.readFileSync(process.argv[2], 'utf8').replace('export const meta', 'const meta')
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor

async function run(args, behaviour = {}) {
  const calls = []
  const logs = []
  const agent = async (prompt, opts) => {
    calls.push({ prompt, opts })
    const label = opts && opts.label
    if (behaviour[label] === null) return null
    return `OUT[${label}]`
  }
  const parallel = async fns => Promise.all(fns.map(f => f()))
  const fn = new AsyncFunction('args', 'agent', 'parallel', 'phase', 'log', 'Date', 'Math', src + '\n')
  const noDate = { now() { throw new Error('Date.now') } }
  const noMath = { ...Object.fromEntries(Object.getOwnPropertyNames(Math).map(k => [k, Math[k]])), random() { throw new Error('Math.random') } }
  try {
    const out = await fn(args, agent, parallel, () => {}, m => logs.push(m), noDate, noMath)
    return { out, calls, logs }
  } catch (e) {
    return { error: e.message, calls, logs }
  }
}

let fails = 0
const ok = (cond, name, extra) => { if (!cond) { fails++; console.log('FAIL', name, extra === undefined ? '' : JSON.stringify(extra).slice(0, 400)) } else console.log('ok  ', name) }

;(async () => {
  // 1. object args, three path reports
  let r = await run({ target: 'doc.md', reports: ['r1.md', 'r2.md', 'r3.md'], claim: 'X holds' })
  ok(!r.error && r.calls.length === 3, '1 three agents (two judges, one compare)', r.error || r.calls.length)
  const [j1, j2, cmp] = r.calls
  ok(j1.opts.label === 'judge:1' && j2.opts.label === 'judge:2' && cmp.opts.label === 'compare', '1 labels')
  ok(j1.prompt.indexOf('Report A\n\nThe file r1.md') > 0 && j1.prompt.indexOf('Report C\n\nThe file r3.md') > 0, '1 run 1 keeps the caller order')
  ok(j2.prompt.indexOf('Report A\n\nThe file r3.md') > 0 && j2.prompt.indexOf('Report C\n\nThe file r1.md') > 0, '1 run 2 reverses it')
  ok(j1.prompt.includes('/dia:dia-adjudicate') && j1.prompt.includes('run 1 of two') && j2.prompt.includes('run 2 of two'), '1 names the skill and the run')
  ok(j1.prompt.includes('The conclusion to judge: "X holds"') && j1.prompt.includes('the document doc.md'), '1 target and claim reach the judge')
  ok(j1.prompt.includes("in the skill's own layout.") && !/table|schema|format wins/i.test(j1.prompt), '1 asks for the skill layout and fixes no format')
  ok(cmp.prompt.includes('OUT[judge:1]') && cmp.prompt.includes('OUT[judge:2]') && cmp.prompt.includes('"report":"r3.md"'), '1 compare gets both outputs and the maps')
  ok(cmp.prompt.includes('"What the verdicts leave of C" section, word for word') && cmp.prompt.indexOf('leave of C') < cmp.prompt.indexOf('Do not judge the items yourself'), '1 compare is asked for both lines on what the verdicts leave of C')
  ok(r.out.differences_and_must_check === 'OUT[compare]' && r.out.judge_runs.length === 2 && r.out.judge_runs[1].map[0].report === 'r3.md', '1 result shape', r.out)
  ok(/have not been checked against the sources/.test(r.out.note), '1 note tells the caller to check')
  ok(r.calls.every(c => !/OUT\[judge:[12]\]/.test(c.prompt) || c.opts.label === 'compare'), '1 no judge sees the other run')

  // 2. strict JSON string
  r = await run('{"target": "doc.md", "reports": ["a.md", "b.md"]}')
  ok(!r.error && r.calls.length === 3 && r.calls[0].prompt.includes('The file a.md'), '2 JSON string args', r.error)
  ok(!r.calls[0].prompt.includes('The conclusion to judge'), '2 no claim sentence without a claim')

  // 3. loose string
  r = await run("{target: 'doc.md', reports: ['a.md', 'b.md'], claim: 'c'}")
  ok(!r.error && r.calls.length === 3 && r.calls[1].prompt.indexOf('Report A\n\nThe file b.md') > 0, '3 loose string args', r.error)

  // 4. missing pieces
  r = await run({ target: 'doc.md' })
  ok(/args\.reports/.test(r.error || '') && r.calls.length === 0, '4 no reports: error before any agent', r.error)
  r = await run({ reports: ['a.md'] })
  ok(/args\.target/.test(r.error || '') && r.calls.length === 0, '4 no target: error', r.error)
  r = await run(undefined)
  ok(/args\.target/.test(r.error || ''), '4 no args: error', r.error)
  r = await run('judge these please')
  ok(/args as an object/.test(r.error || ''), '4 prose string: error naming the shape', r.error)

  // 5. several targets
  r = await run({ targets: ['a.md', 'b.md'], reports: ['r.md'] })
  ok(/args\.claim/.test(r.error || '') && r.calls.length === 0, '5 several targets without a claim: error', r.error)
  r = await run({ targets: ['a.md', 'b.md'], reports: ['r.md'], claim: 'C' })
  ok(!r.error && r.calls[0].prompt.includes('the documents a.md, b.md, read as one text'), '5 several targets with a claim', r.error)
  ok(r.calls.length === 3, '5 one report still gets two runs and a comparison', r.calls.length)

  // 6. inline text reports, mixed with a path and an object
  r = await run({ target: 'doc.md', reports: ['Finding 1\nThe date is wrong.', { path: 'r2.md' }, { text: 'short text report' }] })
  ok(!r.error && r.calls[0].prompt.includes('### Report A\n\nFinding 1\nThe date is wrong.') && r.calls[0].prompt.includes('The file r2.md'), '6 inline text and path', r.error)
  ok(r.calls[0].prompt.includes('### Report C\n\nshort text report'), '6 object text')
  ok(r.out.reports[0] === 'report 1 as given' && r.out.judge_runs[1].map[0].report === 'report 3 as given', '6 text reports are named by position', r.out && r.out.reports)

  // 7. one judge fails
  r = await run({ target: 'doc.md', reports: ['a.md', 'b.md'] }, { 'judge:2': null })
  ok(!r.error && r.calls.length === 2 && r.out.differences_and_must_check === null && /Only 1 of 2/.test(r.out.note) && r.logs.length === 1, '7 one judge missing: no comparison, a note', r.error || r.out)
  ok(r.out.judge_runs[0].output === 'OUT[judge:1]', '7 the run that returned is passed on')

  // 8. comparison fails
  r = await run({ target: 'doc.md', reports: ['a.md', 'b.md'] }, { compare: null })
  ok(!r.error && r.out.differences_and_must_check === null && /Compare the two judge runs above yourself/.test(r.out.note), '8 comparison missing: a note', r.error || r.out)

  // 10. quotes inside values
  r = await run('{target: "doc.md", reports: ["r.md"], claim: "The agency\'s ban holds"}')
  ok(!r.error && r.calls[0].prompt.includes('The conclusion to judge: "The agency\'s ban holds"'), '10 an apostrophe in a double-quoted claim survives', r.error)
  r = await run("{target: 'doc.md', reports: ['r.md'], claim: 'the \"ban\" holds'}")
  ok(/args as an object/.test(r.error || '') && r.calls.length === 0, '10 mixed quotes that cannot be read: error, no agent', r.error)

  // 11. report entries
  r = await run({ target: 'doc.md', reports: ['a.md', 'b.md', 'a.md'] })
  ok(/same report file twice/.test(r.error || '') && r.calls.length === 0, '11 a repeated report path: error', r.error)
  r = await run({ target: 'doc.md', reports: [{ file: 'a.md' }, 'b.md'] })
  ok(/report 1 in args\.reports/.test(r.error || '') && r.calls.length === 0, '11 an entry that is neither path nor text: error naming it', r.error)
  r = await run({ target: 'doc.md', reports: ['my reviews/report one.md', 'b.md'] })
  ok(!r.error && r.calls[0].prompt.includes('The file my reviews/report one.md. Read it in full.'), '11 a path with spaces is kept', r.error)
  r = await run({ target: 'doc.md', reports: ['S2 is wrong: 0.9 times 20 is 18, not 9.', 'b.md'] })
  ok(!r.error && r.calls[0].prompt.includes('The file S2 is wrong'), '11 a one-line string is a path; text goes in {text}')

  // 12. targets
  r = await run({ target: 'doc.md', targets: ['doc.md', ' doc.md '], reports: ['r.md'] })
  ok(!r.error && r.out.targets.length === 1 && r.calls[0].prompt.includes('the document doc.md'), '12 the same target twice is one target', r.error)
  r = await run({ target: '   ', reports: ['r.md'] })
  ok(/args\.target/.test(r.error || '') && r.calls.length === 0, '12 a blank target: error', r.error)

  // 13. no judge returns
  r = await run({ target: 'doc.md', reports: ['a.md', 'b.md'] }, { 'judge:1': null, 'judge:2': null })
  ok(!r.error && r.calls.length === 2 && /Neither dia-adjudicate run returned/.test(r.out.note), '13 no judge returned: the note says to start again', r.error || r.out)

  // 14. the note on a complete run
  r = await run({ target: 'doc.md', reports: ['a.md', 'b.md'] })
  ok(/Report every item on which the two runs differ, and the must-check list/.test(r.out.note), '14 the note asks for every differing item and the must-check list')

  // 9. too many reports
  r = await run({ target: 'doc.md', reports: Array.from({ length: 27 }, (_, i) => `r${i}.md`) })
  ok(/at most 26/.test(r.error || ''), '9 more than 26 reports: error', r.error)

  console.log(fails ? `${fails} FAILED` : 'ALL OK')
  process.exit(fails ? 1 : 0)
})()
