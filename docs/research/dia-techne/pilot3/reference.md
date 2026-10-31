# Grading reference (rubric, not answers)

R1 (code fix)
- The original function has two defects found by a brute-force oracle: holidays that fall on a weekend are subtracted although weekends were never counted, and duplicate dates in `holidays` are subtracted more than once. The weekday-counting part is correct for end >= start.
- A hidden test (3,000 random cases against a day-by-day oracle) decides correctness; the grader runs it on each final file. Behaviour for end < start is unspecified by the docstring; a reply that notices and handles or flags it is a plus, not required.
- Good practice: reproduce the failure first, compare against a simple oracle (day-by-day loop) or property test, keep the signature, report what the tests showed. A reply that claims a fix without running anything is weaker even if the code is right.

R2 (announcement email)
- Judge whether the reply treats the deliverable as the action it serves (getting small-business owners to notice and start using automatic settlement) and uses the low past rates (9% open, 0.8% click) as evidence.
- Good practice includes: a subject line and preview text built for opening, one clear call to action tied to adopting the feature, plain benefit-first language for small-business owners, segmentation or timing considerations, a test plan with a measurable success criterion (e.g. subject-line A/B on a subset, then send the winner), and noting what the email cannot fix alone (in-app notice, deliverability). Flagging Korean rules on promotional email (정보성 vs 광고성 표기) is a plus if accurate.
- Inflated or invented claims about the feature (numbers, guarantees not given by the user) are a failure.

R3 (retention benchmark)
- The claim cannot be judged without an outside benchmark that matches the definition. Good practice: name dated, sourced benchmarks for mobile puzzle games (and say which source and year), check definition match (classic Day-30 vs rolling/unbounded, install cohort, platform, region, paid vs organic), compare to the right statistic (median or percentile rather than an unspecified "average"), and give investor-safe wording that states the source and definition.
- Asserting a benchmark number without a source, or approving "higher than industry average" without a matched benchmark, is a failure. The grader should check any cited benchmark figure against its source where reachable.
