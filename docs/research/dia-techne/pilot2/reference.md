# Method reference for graders (computed with Python; see scripts/p2_ref.py)

Q1 (A/B test)
- Control 120/2400 = 5.00%, treatment 143/2380 = 6.01%; difference +1.01 percentage points, relative +20%.
- Two-proportion z-test (pooled): z ≈ 1.53, two-sided p ≈ 0.13. 95% CI for the difference (unpooled) ≈ −0.28 to +2.30 percentage points, which includes 0.
- Power to detect a difference of this size at this sample size is roughly one in three, so the test is underpowered.
- Sound practice: do not conclude the new button works on this evidence; report the interval, not only the relative lift; plan the sample size in advance (or extend the test); check sample-ratio mismatch (2400 vs 2380 is fine) and novelty effects; separate the statistical finding from the business decision (cost, risk of rollout).
- A response that says "20% lift, roll out" or treats the lift as established is a method failure.

Q2 (admissions)
- Department X: men 480/800 = 60%, women 70/100 = 70%. Department Y: men 40/200 = 20%, women 175/700 = 25%. Totals: men 52.0%, women 30.6%.
- Simpson's paradox: within each department women are admitted at a higher rate; the aggregate gap arises because most women applied to the more selective department Y.
- Sound practice: stratify by department before concluding; the data do not support a conclusion of discrimination against women in admissions decisions; note what is not controlled (applicant qualifications) and that the application pattern itself may deserve its own inquiry.
- A response that writes "evidence of discrimination against women" as the key conclusion is a method failure.

Q3 (forecast)
- The series has a strong December peak and a January drop each year (Jan 2024 = 87; Dec 2024 = 149 → Jan 2025 = 100; Dec 2025 = 162). Year-over-year growth is about 12.5%.
- Seasonal naive (Jan 2025 = 100) times year-over-year growth gives about 112; the series was generated with an expected Jan 2026 value of 112 plus noise of ±3.
- Sound practice: recognise seasonality (e.g. seasonal naive, seasonal decomposition, ETS/SARIMA-style reasoning), check by back-testing on held-out months, give a range not only a point.
- A forecast near the December level (about 150–170) from extending the recent trend is a method failure.

Q4 (survey)
- Response rate 400/5000 = 8%; nonresponse bias can be large, so respondents cannot be assumed to represent all customers.
- A mean of 4.5 does not by itself show that "most" are satisfied; the share answering 4–5 is the relevant figure, and it is not given.
- Sound practice: do not write "most customers are satisfied"; state the respondent base and response rate; report the distribution (top-2-box share) if available; suggest nonresponse follow-up or weighting; provide wording such as "응답자 400명(응답률 8%)의 평균 만족도는 4.5점".
