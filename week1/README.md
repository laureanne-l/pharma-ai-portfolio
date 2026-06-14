# Clinical Trials Analysis
### Analysing 100 cancer trials from the ClinicalTrials.gov API

---

## What This Is
A Python and pandas analysis of 100 cancer-related clinical trials, 
sourced live from the ClinicalTrials.gov API. Built as part of a 
self-directed technical learning programme in AI and pharma strategy.

The goal was to answer five questions a pharma strategist would actually 
ask — not just to demonstrate coding ability, but to develop the instinct 
for what real clinical data looks like and what it can and can't tell you.

---

## Data Source
- **Source:** ClinicalTrials.gov public API (v2)
- **Query:** Cancer trials, paginated across 5 API calls
- **Retrieved:** May 2026
- **Raw dataset:** 100 trials, 137 fields each
- **Analysis dataset:** 55 trials after cleaning (see Methodology)

---

## Key Findings

**1. Cancer research is predominantly publicly funded**
66% of trials were funded by non-industry sources (academic, NIH, 
government). Industry funded only 28%. NIH-funded trials had the 
highest median enrollment at 175 patients — nearly double industry 
trials at 96 patients.

**2. Phase 3 trials are dramatically larger than earlier phases**
Median enrollment: Phase 3 = 644 patients, Phase 2 = 47 patients, 
Phase 1 = 24 patients. The jump from Phase 2 to Phase 3 reflects the 
statistical power required for regulatory submission.

**3. Trials take longer than most people assume**
Median time from start to primary completion: 38.5 months (~3.2 years). 
Full trial completion including follow-up: 50.5 months (~4.2 years). 
Even early-phase cancer trials rarely complete in under 2 years.

**4. Phase 2 is the shortest phase by design**
Median Phase 2 duration: 30 months vs Phase 3: 41 months. This reflects 
the "fail fast" philosophy in oncology — Phase 2 trials are designed to 
identify non-responders quickly and stop early if there's no signal.

**5. Nearly half the dataset was observational research**
24 of 100 trials were observational studies with no phase designation — 
a reminder that ClinicalTrials.gov captures far more than the 
Phase 1→2→3 pipeline most people picture.

---

## Methodology & Data Cleaning

The raw dataset required significant cleaning before analysis. 
All exclusion decisions are documented and justified below.

**What was excluded and why:**

| Reason | Count |
|---|---|
| Observational studies (no phase by design) | 24 |
| Interventional trials with no phase recorded | 21 |
| Trials with missing enrollment data | 1 |
| Withdrawn trials with 0 enrollment | 1 |
| **Total excluded** | **45** |

**How exclusions were verified:**
Each exclusion category was confirmed by checking the raw data — 
not assumed. For example, the 24 trials with no phase were confirmed 
as observational studies by checking the `study_type` field directly. 
The 21 interventional trials with no phase are likely expanded access 
or registry studies.

**Statistical notes:**
- Phase 1 enrollment: mean 72 vs median 24 — significant right skew 
  driven by one 416-patient basket trial. Median is the more honest figure.
- Phase 3 enrollment: mean 697 vs median 644 — mild skew, both figures reliable.
- Early Phase 1 duration excluded from conclusions — only 2 trials, 
  insufficient for meaningful analysis.


---

## What This Means for Pharma AI Strategy

Three implications that emerge directly from this data:

**1. Trial acceleration is the highest-value AI application.** At typical 
Phase 3 costs, cutting the 38.5-month median by 20% through AI-assisted 
patient selection and site optimisation represents hundreds of millions 
in value per programme.

**2. The public funding dominance in oncology creates unusual dynamics.** 
AI tools that serve academic and NIH-funded research — not just industry — 
will capture a larger share of the cancer trial market than tools built 
purely for pharma sponsors.

**3. Phase 2 "fail fast" design is where AI signal-finding matters most.** 
The 30-month median suggests these trials are already optimised for speed. 
AI biomarker identification could compress this further — or more 
importantly, improve the signal quality so fewer drugs fail in Phase 3.

**4. Clinical AI models may already be training on outdated data.**
With a median of 50.5 months to full trial completion, data from trials 
started today won't be fully available until 2030. AI models being built 
now are largely trained on trials that started 5-10 years ago, under 
different protocols, populations, and standards of care. Data freshness 
is an underappreciated risk in clinical AI — one that rarely appears in 
vendor pitches.

**5. Real-world evidence is the next frontier.**
24% of this dataset was observational research — and this proportion is 
growing as regulators increasingly accept real-world evidence alongside 
randomised trials. AI that can extract reliable signal from messy 
observational data is arguably more valuable than AI optimising clean 
Phase 3 trials. The commercial opportunity follows the data complexity.

**6. Basket trials are quietly reshaping the early pipeline.**
One Phase 1 trial in this dataset enrolled 416 patients — 17x the median. 
These are basket trials: testing one drug across multiple tumour types 
simultaneously, enabled by AI-assisted patient matching. They compress 
the early development timeline significantly and represent one of the 
clearest current examples of AI changing trial design itself, not just 
trial operations.

---

## Technical Stack

- **Python 3.14** — core analysis language
- **pandas** — data manipulation and cleaning
- **matplotlib** — data visualisation
- **requests** — live API calls to ClinicalTrials.gov
- **Jupyter notebook** — interactive analysis environment
- **Cursor** — AI-assisted development environment

## Files

- `clinical_trial_analysis_clean.ipynb` — full analysis notebook
- `trials.csv` — raw data snapshot from ClinicalTrials.gov (May 2026)

---

*Analysis based on publicly available data from ClinicalTrials.gov. 
Retrieved May 2026. Sample size (55 trials) is illustrative — 
conclusions should not be generalised beyond this dataset without 
further validation.*