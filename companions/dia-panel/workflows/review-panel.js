export const meta = {
  name: 'review-panel',
  description: 'Review one document with four dia lenses in parallel, then judge their whole reports twice with dia-adjudicate',
  whenToUse: 'When the user asks for a dia review panel on a document. args: {target: "path/to/doc.md", claim: "optional central claim"}',
  phases: [{ title: 'Lenses' }, { title: 'Judge' }, { title: 'Compare' }],
}

let a = args || {}
if (typeof a === 'string') {
  const s = a.trim()
  if (s.startsWith('{')) {
    // A Skill-tool call may pass {target: "..."} as text that is not strict JSON.
    try { a = JSON.parse(s) } catch (e) {
      const pick = k => (s.match(new RegExp(`${k}\\s*["']?\\s*:\\s*["']([^"']+)["']`)) || [])[1]
      a = { target: pick('target') || s, claim: pick('claim') }
    }
  } else {
    a = { target: s }
  }
}
const target = a.target
if (!target) throw new Error('review-panel needs args.target (path of the document to review)')
const claim = a.claim ? ` The central claim to examine: "${a.claim}".` : ''

const LENSES = [
  { key: 'negative', skill: 'dia:dia-negative' },
  { key: 'reductio', skill: 'dia:dia-reductio' },
  { key: 'warrant', skill: 'dia:dia-warrant' },
  { key: 'counterplan', skill: 'dia:dia-counterplan' },
]

const lensPrompt = l =>
  `Use the /${l.skill} skill on the document ${target} (target: text).${claim} ` +
  `Give the whole result in one response, with no questions: no person will answer. ` +
  `Your final text is passed unchanged to a judge, so return the skill's complete output in its own layout, ` +
  `not a summary and not a findings table.`

phase('Lenses')
const reports = await parallel(LENSES.map(l => () =>
  agent(lensPrompt(l), { label: `lens:${l.key}`, phase: 'Lenses' }).then(text => ({ key: l.key, text }))))
const got = reports.filter(r => r && r.text)
const missing = LENSES.map(l => l.key).filter(k => !got.some(r => r.key === k))
if (missing.length) log(`No report from: ${missing.join(', ')}`)
if (got.length === 0) throw new Error('no lens returned a report')

// Two fixed orders (Math.random is not available in workflows): the second reverses the first, a counterbalance, not a random shuffle.
// Reports carry letters, not R numbers, because dia-adjudicate relabels its reports R1..Rn itself.
const LETTERS = 'ABCD'
const order1 = got.map((_, i) => i).sort((x, y) => ((x * 7 + 3) % 5) - ((y * 7 + 3) % 5))
const order2 = [...order1].reverse()
const block = order => order.map((idx, n) => `### Report ${LETTERS[n]}\n\n${got[idx].text}`).join('\n\n')
const mapOf = order => order.map((idx, n) => ({ label: LETTERS[n], lens: got[idx].key }))

const judgePrompt = (order, k) =>
  `Use the /dia:dia-adjudicate skill. Target T: the document ${target}.${claim} ` +
  `The reports below are given whole and carry letters only; each still names its own method. This is run ${k} of two separate runs on the same input; ` +
  `the caller compares the two, so start no run of your own. No person will answer: give the whole result in one response.\n\n` +
  block(order)

phase('Judge')
const judged = await parallel([1, 2].map(k => () =>
  agent(judgePrompt(k === 1 ? order1 : order2, k), { label: `judge:${k}`, phase: 'Judge' })))
const judgeRuns = [{ map: mapOf(order1), output: judged[0] }, { map: mapOf(order2), output: judged[1] }]
const result = {
  target,
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
    note: `Only ${okJudges} of 2 dia-adjudicate runs returned, so no comparison was made. Run dia-adjudicate again on the lens reports in a separate agent, then compare the two runs (dia-adjudicate, Running twice).`,
  }
}

phase('Compare')
const [diff] = await parallel([() => agent(
  `Two independent runs of dia-adjudicate judged the same reports on ${target}. ` +
  `The caller gave the reports letters: run 1 ${JSON.stringify(mapOf(order1))}, run 2 ${JSON.stringify(mapOf(order2))}. ` +
  `Each run may relabel the reports again (R1, R2, ...); its Inputs line maps its labels to the letters. ` +
  `Match report items by lens (not by any label) and claims in the target by their place in it. ` +
  `List every item whose verdict differs between the runs, with both verdicts and their stated basis, ` +
  `then the union of both must-check lists. Do not judge the items yourself.\n\n` +
  `## Run 1\n\n${judged[0]}\n\n## Run 2\n\n${judged[1]}`,
  { label: 'compare', phase: 'Compare' })])

return {
  ...result,
  differences_and_must_check: diff,
  note: diff
    ? 'The verdicts that differ between the two runs have not been checked against the sources. Check each against the source it rests on before relying on it (dia-adjudicate, Running twice).'
    : 'The comparison agent returned nothing. Compare the two judge runs above yourself, and check each verdict that differs against the source it rests on (dia-adjudicate, Running twice).',
}
