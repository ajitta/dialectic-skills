export const meta = {
  name: 'judge',
  description: 'Judge reports that reviewers or agents already wrote about a document: dia-adjudicate twice in separate agents, with the reports in two orders, then the verdicts that differ',
  whenToUse: 'When reports about a document exist (from review agents, another assistant or people) and need a ruling. Use this instead of starting one dia-adjudicate agent yourself: it makes the two runs and the comparison that a judge inside an agent often cannot start itself. args: {target: "path/to/doc.md", reports: ["path/to/report-1.md", "path/to/report-2.md"], claim: "optional conclusion to judge"}. A report held in memory: {text: "..."} in place of a path. Several documents: targets: [...] with claim.',
  phases: [{ title: 'Judge' }, { title: 'Compare' }],
}

let a = args || {}
if (typeof a === 'string') {
  // A Skill-tool call may pass the arguments as text that is not strict JSON: unquoted keys, or single quotes.
  // Single quotes are turned into double quotes only when the text has no double quote, so an apostrophe
  // inside a double-quoted claim is left alone.
  const s = a.trim()
  const keyed = s.replace(/([{,]\s*)([A-Za-z_]\w*)\s*:/g, '$1"$2":')
  const forms = s.includes('"') ? [s, keyed] : [s, keyed, keyed.replace(/'/g, '"')]
  let parsed = null
  for (const t of forms) {
    try { parsed = JSON.parse(t); break } catch (e) { /* try the next form */ }
  }
  if (!parsed || typeof parsed !== 'object') {
    throw new Error('judge needs args as an object: {target: "doc.md", reports: ["report-1.md", "report-2.md"], claim: "optional"}')
  }
  a = parsed
}
const list = v => (Array.isArray(v) ? v : v ? [v] : [])
const targets = [...new Set([...list(a.target), ...list(a.targets)].map(t => String(t).trim()).filter(Boolean))]
if (targets.length === 0) throw new Error('judge needs args.target (path of the document the reports are about)')
if (targets.length > 1 && !a.claim) {
  throw new Error('judge needs args.claim when there are several target documents: the conclusion the reports are judged against')
}

// A report is a file path (a string, or {path}), or the report's own text when the caller holds it in
// memory ({text}, or a string with a line break). An entry that is neither stops the run, so that no
// report is left out without the caller knowing.
const asReport = (r, i) => {
  if (r && typeof r === 'object' && typeof r.text === 'string' && r.text.trim()) return { text: r.text }
  if (r && typeof r === 'object' && typeof r.path === 'string' && r.path.trim()) return { path: r.path.trim() }
  if (typeof r === 'string' && r.trim()) return r.includes('\n') ? { text: r } : { path: r.trim() }
  throw new Error(`judge cannot read report ${i + 1} in args.reports: give a file path, {path: "..."} or {text: "..."}`)
}
const reports = list(a.reports).map(asReport)
if (reports.length === 0) throw new Error('judge needs args.reports (paths of the report files, or {text: "..."} for a report held in memory)')
const paths = reports.filter(r => r.path).map(r => r.path)
if (new Set(paths).size !== paths.length) throw new Error('judge was given the same report file twice in args.reports')
const LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if (reports.length > LETTERS.length) throw new Error(`judge takes at most ${LETTERS.length} reports`)

const targetText = targets.length === 1
  ? `the document ${targets[0]}`
  : `the documents ${targets.join(', ')}, read as one text`
const claim = a.claim ? ` The conclusion to judge: "${a.claim}".` : ''

// Two fixed orders (Math.random is not available in workflows): the caller's order and its reverse, a counterbalance, not a random shuffle.
// Reports carry letters, not R numbers, so that a judge's own labels (if it gives any) cannot be confused with the caller's.
const order1 = reports.map((_, i) => i)
const order2 = [...order1].reverse()
const name = idx => reports[idx].path || `report ${idx + 1} as given`
const mapOf = order => order.map((idx, n) => ({ label: LETTERS[n], report: name(idx) }))
const block = order => order.map((idx, n) => {
  const r = reports[idx]
  return r.path
    ? `### Report ${LETTERS[n]}\n\nThe file ${r.path}. Read it in full.`
    : `### Report ${LETTERS[n]}\n\n${r.text}`
}).join('\n\n')

const judgePrompt = (order, k) =>
  `Use the /dia:dia-adjudicate skill. Target T: ${targetText}.${claim} ` +
  `The reports below are given whole and carry letters only; rule on what a report says, not on its file name. ` +
  `This is run ${k} of two separate runs on the same input; the caller compares the two, so start no run of your own. ` +
  `No person will answer: give the whole result in one response, in the skill's own layout.\n\n` +
  block(order)

phase('Judge')
const judged = await parallel([1, 2].map(k => () =>
  agent(judgePrompt(k === 1 ? order1 : order2, k), { label: `judge:${k}`, phase: 'Judge' })))
const result = {
  targets,
  reports: reports.map((_, idx) => name(idx)),
  judge_runs: [{ map: mapOf(order1), output: judged[0] }, { map: mapOf(order2), output: judged[1] }],
}

const okJudges = judged.filter(Boolean).length
if (okJudges < 2) {
  log(`Only ${okJudges} of 2 judge runs returned; no comparison was made`)
  return {
    ...result,
    differences_and_must_check: null,
    note: okJudges === 0
      ? 'Neither dia-adjudicate run returned, so there is no ruling. Start the workflow again.'
      : 'Only 1 of 2 dia-adjudicate runs returned, so no comparison was made. Run dia-adjudicate again on the reports in a separate agent, then compare the two runs (dia-adjudicate, Where the ruling may be wrong).',
  }
}

phase('Compare')
const [diff] = await parallel([() => agent(
  `Two independent runs of dia-adjudicate judged the same reports on ${targetText}. ` +
  `The caller gave the reports letters: run 1 ${JSON.stringify(mapOf(order1))}, run 2 ${JSON.stringify(mapOf(order2))}. ` +
  `Each run may relabel the reports again (R1, R2, ...); its opening lines say what it took as each report. ` +
  `Match report items by report (not by any label) and claims in the target by their place in it. ` +
  `List every item whose verdict differs between the runs, with both verdicts and their stated basis, ` +
  `then the union of both runs' lists of where the ruling may be wrong, then each run's statement of what its rulings leave of the target's conclusion, word for word (every line of it), ` +
  `and whether the two give the same outcome for the conclusion (say so if a run gives no such statement). Do not judge the items yourself.\n\n` +
  `## Run 1\n\n${judged[0]}\n\n## Run 2\n\n${judged[1]}`,
  { label: 'compare', phase: 'Compare' })])

return {
  ...result,
  differences_and_must_check: diff,
  note: diff
    ? 'Report every item on which the two runs differ, and the lists of where the ruling may be wrong, to the person who decides, together with each run\'s statement of what its rulings leave of the target\'s conclusion. The differing verdicts have not been checked against the sources: check each against the source it rests on before relying on it, and say which reading is your own (dia-adjudicate, Where the ruling may be wrong).'
    : 'The comparison agent returned nothing. Compare the two judge runs above yourself, and check each verdict that differs against the source it rests on (dia-adjudicate, Where the ruling may be wrong).',
}
