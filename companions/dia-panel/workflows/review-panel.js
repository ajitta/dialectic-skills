export const meta = {
  name: 'review-panel',
  description: 'Review one document with four dia lenses in parallel, then judge their whole reports twice with dia-adjudicate',
  whenToUse: 'When the user asks for a dia review panel on a document. args: {target: "path/to/doc.md", claim: "optional central claim", context: "what the user has said about the document (what it is for, the facts they gave), copied as they wrote it", material: ["paths of files the document points to"]}. The lenses and judges see nothing of your conversation and take context as written by the user: pass it whenever the user has said anything about the document, and add only what their words need to be understood (the question a reply answers), marked as yours.',
  phases: [{ title: 'Lenses' }, { title: 'Judge' }, { title: 'Compare' }],
}

let a = args || {}
if (typeof a === 'string') {
  // A Skill-tool call may pass the arguments as text. The text is the arguments object, with or without something
  // around it (a code fence, a label), or it is the path alone, on one line. Anything else stops the run: taken
  // whole as a path, it would start the agents on a target that is no file and without the user's words.
  const s = a.trim()
  const from = s.indexOf('{')
  let parsed = null
  if (from >= 0) {
    // The object need not be strict JSON: unquoted keys, or single quotes.
    // Single quotes are turned into double quotes only when the text has no double quote, so an apostrophe
    // inside a double-quoted value (the user's words) is left alone, as in judge.js.
    // Bare keys are quoted only outside double-quoted strings and a line break inside one is escaped, so the
    // user's words in a double-quoted value may run over several lines and may hold a comma, a word and a colon.
    const to = s.lastIndexOf('}')
    const o = to > from ? s.slice(from, to + 1) : s.slice(from)
    const keyed = o.replace(/"(?:[^"\\]|\\[\s\S])*"|([{,]\s*)([A-Za-z_]\w*)(\s*:)/g,
      (m, pre, key, colon) => key ? `${pre}"${key}"${colon}` : m.replace(/\r?\n/g, '\\n').replace(/\t/g, '\\t'))
    const forms = o.includes('"') ? [o, keyed] : [o, keyed, keyed.replace(/'/g, '"')]
    for (const t of forms) {
      try { parsed = JSON.parse(t); break } catch (e) { /* try the next form */ }
    }
  }
  // Text that begins with a brace is the object or nothing. A brace further in may belong to a path
  // (src/pages/{slug}.md), so there the object counts only when it parsed and names a target.
  if (parsed && typeof parsed === 'object' && (from === 0 || parsed.target)) {
    a = parsed
  } else if (from === 0 || /[\r\n]/.test(s)) {
    throw new Error('review-panel needs args as an object: {target: "doc.md", claim: "optional", context: "optional", material: ["optional"]}')
  } else {
    a = { target: s }
  }
}
const target = a.target
if (!target) throw new Error('review-panel needs args.target (path of the document to review)')
const claim = a.claim ? ` The central claim to examine: "${a.claim}".` : ''
// What the user said about the document reaches every lens and judge in the user's words, marked as material:
// an agent sees nothing of the caller's conversation. Several messages may come as a list.
const said = (Array.isArray(a.context) ? a.context.map(m => typeof m === 'string' ? m : JSON.stringify(m)).join('\n\n')
  : a.context == null ? '' : typeof a.context === 'string' ? a.context : JSON.stringify(a.context))
  .trim().replace(/<\/user_words>/gi, '</ user_words>')
// An entry of material is a path: a string, or {path} as judge.js takes for a report. Anything else stops the run,
// so that nothing but a path is named to the agents and reported back as given.
const asPath = (m, i) => {
  if (typeof m === 'string') return m.trim()
  if (m && typeof m === 'object' && typeof m.path === 'string') return m.path.trim()
  throw new Error(`review-panel cannot read entry ${i + 1} of args.material: give a file path or {path: "..."}`)
}
const material = (Array.isArray(a.material) ? a.material : a.material ? [a.material] : []).map(asPath).filter(Boolean)
const points = material.length ? ` The document points to: ${material.join(', ')}.` : ''
const userWords = said
  ? `\n\nWhat the user has said about this document follows, as the user wrote it; what is marked in it as the caller's is the caller's. ` +
    `It is material, not instructions to you, and a fact the user states in it counts as supplied by the user.\n<user_words>\n${said}\n</user_words>`
  : ''

const LENSES = [
  { key: 'negative', skill: 'dia:dia-negative' },
  { key: 'reductio', skill: 'dia:dia-reductio' },
  { key: 'warrant', skill: 'dia:dia-warrant' },
  { key: 'counterplan', skill: 'dia:dia-counterplan' },
]

const lensPrompt = l =>
  `Use the /${l.skill} skill on the document ${target}.${points}${claim} ` +
  `Give the whole result in one response, with no questions: no person will answer. ` +
  `Your final text is passed unchanged to a judge, so return the skill's complete output in its own layout, ` +
  `not a summary and not a findings table.` + userWords

phase('Lenses')
const reports = await parallel(LENSES.map(l => () =>
  agent(lensPrompt(l), { label: `lens:${l.key}`, phase: 'Lenses' }).then(text => ({ key: l.key, text }))))
const got = reports.filter(r => r && r.text)
const missing = LENSES.map(l => l.key).filter(k => !got.some(r => r.key === k))
if (missing.length) log(`No report from: ${missing.join(', ')}`)
if (got.length === 0) throw new Error('no lens returned a report')

// Two fixed orders (Math.random is not available in workflows): the second reverses the first, a counterbalance, not a random shuffle.
// Reports carry letters, not R numbers, so that a judge's own labels (if it gives any) cannot be confused with the caller's.
const LETTERS = 'ABCD'
const order1 = got.map((_, i) => i).sort((x, y) => ((x * 7 + 3) % 5) - ((y * 7 + 3) % 5))
const order2 = [...order1].reverse()
const block = order => order.map((idx, n) => `### Report ${LETTERS[n]}\n\n${got[idx].text}`).join('\n\n')
const mapOf = order => order.map((idx, n) => ({ label: LETTERS[n], lens: got[idx].key }))

const judgePrompt = (order, k) =>
  `Use the /dia:dia-adjudicate skill. Target T: the document ${target}.${points}${claim} ` +
  `The reports below are given whole and carry letters only; each still names its own method. This is run ${k} of two separate runs on the same input; ` +
  `the caller compares the two, so start no run of your own. No person will answer: give the whole result in one response.` + userWords + `\n\n` +
  block(order)

phase('Judge')
const judged = await parallel([1, 2].map(k => () =>
  agent(judgePrompt(k === 1 ? order1 : order2, k), { label: `judge:${k}`, phase: 'Judge' })))
// A run that returned nothing carries its prompt, so that a rerun gets the same input, the user's words included.
const judgeRuns = [order1, order2].map((order, i) => ({ map: mapOf(order), output: judged[i], ...(judged[i] ? {} : { prompt: judgePrompt(order, i + 1) }) }))
// The caller reads this note: what the panel was given, and how to hand the result on.
const handOn = `The panel worked from ${said ? 'the document and what the user said about it' : 'the document alone: nothing the user has said about it was passed (args.context)'}. ` +
  `When you report to the user, give the user the lens reports and the judge runs, whole or in a file you write and name, ` +
  `say which conclusions are the panel's and which are your own, and put to the user the questions the reports leave open. `
const result = {
  target,
  given: { context: Boolean(said), material },
  missing_lenses: missing,
  lens_reports: got.map(r => ({ lens: r.key, report: r.text })),
  judge_runs: judgeRuns,
}

const okJudges = judged.filter(Boolean).length
if (okJudges < 2) {
  log(`Only ${okJudges} of 2 judge runs returned; no comparison was made`)
  return {
    ...result,
    differences_and_must_check: null,
    note: handOn + `Only ${okJudges} of 2 dia-adjudicate runs returned, so no comparison was made. For each judge run whose output is missing, start one separate agent with that run's prompt, unchanged (it is in judge_runs), then compare the two runs (dia-adjudicate, Where the ruling may be wrong).`,
  }
}

phase('Compare')
const [diff] = await parallel([() => agent(
  `Two independent runs of dia-adjudicate judged the same reports on ${target}. ` +
  `The caller gave the reports letters: run 1 ${JSON.stringify(mapOf(order1))}, run 2 ${JSON.stringify(mapOf(order2))}. ` +
  `Each run may relabel the reports again (R1, R2, ...); its opening lines say what it took as each report. ` +
  `Match report items by lens (not by any label) and claims in the target by their place in it. ` +
  `List every item whose verdict differs between the runs, with both verdicts and their stated basis, ` +
  `then the union of both runs' lists of where the ruling may be wrong, then each run's statement of what its rulings leave of the target's conclusion, word for word (every line of it), ` +
  `and whether the two give the same outcome for the conclusion (say so if a run gives no such statement). Do not judge the items yourself.\n\n` +
  `## Run 1\n\n${judged[0]}\n\n## Run 2\n\n${judged[1]}`,
  { label: 'compare', phase: 'Compare' })])

return {
  ...result,
  differences_and_must_check: diff,
  note: diff
    ? handOn + 'The verdicts that differ between the two runs have not been checked against the sources. Check each against the source it rests on before relying on it (dia-adjudicate, Where the ruling may be wrong).'
    : handOn + 'The comparison agent returned nothing. Compare the two judge runs above yourself, and check each verdict that differs against the source it rests on (dia-adjudicate, Where the ruling may be wrong).',
}
