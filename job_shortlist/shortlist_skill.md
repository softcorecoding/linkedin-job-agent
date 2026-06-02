---
name: job-shortlist
description: First-pass LinkedIn job search shortlisting: scan search results, reject hard exclusions, and save plausibly relevant jobs for later fit evaluation.
---

## Goal

Review a LinkedIn jobs listing page and save plausibly relevant jobs for later fit evaluation.

This is a broad first-pass collection workflow. It should:

- use `job_shortlist/profile.md` only
- skip hard exclusions and clear non-matches
- save plausible jobs, including borderline-plausible jobs
- avoid fit scoring, ranking, unsaving, or evidence-bank analysis

## Required File

- `job_shortlist/profile.md`: shortlist profile with candidate summary, hard exclusions, and save signals.

Do not read `tailor_cv/experience_bank.md` during normal shortlisting.

## Shortlist Decision

Read `job_shortlist/profile.md` before reviewing jobs.

- **Skip** when a hard exclusion in `profile.md` applies.
- **Skip** when the poster is clearly a spammy job agency.
- **Skip** when the job clearly has no meaningful connection to the Candidate Evidence Anchors in `profile.md`.
- **Save** when no hard exclusion applies and the role has a real connection to at least one Candidate Evidence Anchor.
- **Save borderline-plausible jobs** when the role might fit but would need deeper evidence-based evaluation later.
- **Uncertain** only when the page, language, role scope, or UI state prevents a safe save/skip decision.

Use only these statuses: `pending`, `saved`, `skipped`, `duplicate`, `uncertain`.

## LinkedIn Navigation

Follow the shared rules in `linkedin.md` (browser visibility, cadence, stop conditions, list pagination, and completion across all pages). For shortlisting, an "item" is a result card.

Shortlist-specific note:

- Click visible cards from the left-side results list; do not repeatedly edit URLs with `currentJobId`.

## Review Tracker

Keep a compact internal tracker so loaded cards are not missed or reviewed twice.

Track only:

- page/start offset
- job ID if visible in a `/jobs/view/<id>/` URL
- title
- company
- location/work mode if visible
- status

Use job ID for de-duplication. If no ID is available, use title + company + location. Mark duplicates as `duplicate` and do not open them again.

Do not show the full tracker to the user unless asked.

## Workflow

1. Open the LinkedIn jobs listing URL and make the browser visible.
2. Read `job_shortlist/profile.md`.
3. On each result page, scroll inside the left-side results list (per List Pagination in `linkedin.md`) until new cards stop loading and the bottom of the list, including the numbered pagination row, is reached.
4. Add each loaded card to the Review Tracker before opening details.
5. Mark duplicates and obvious card-level skips before opening job details.
6. For each remaining pending card, click the visible card and wait for the detail panel to load.
7. Read job detail to apply the Shortlist Decision. Focus on the job description; ignore the "About the company" section. Skip immediately if the job description or requirements are not in English.
8. Save plausible jobs using the Save Button Rules below.
9. Mark ambiguous jobs as `uncertain` and continue. Do not stop mid-run for fit questions.
10. When the current page has no pending tracked cards, advance to the next page using List Pagination in `linkedin.md`. Do not stop just because the current page is done.
11. Repeat across all numbered result pages. Do not ask whether to continue between pages.
12. Before ending, apply Completion Across All Pages and the result-count gate from `linkedin.md`: the left list has been fully scrolled, no higher-numbered page or Next control remains, no pending tracked cards remain, and the unique handled count approaches the visible total — unless LinkedIn blocked access or a stop condition occurred.

## Save Button Rules

- Prefer the exact accessible button: `Save <job title> at <company>`.
- Confirm there is exactly one visible Save button for the active job before clicking.
- If LinkedIn exposes duplicate Save buttons, scroll back to the top of the detail panel and use the clearly visible Save beside Apply.
- Never click Save by coordinates.
- If a job already says `Saved`, do not click again; mark it `saved` and move on.
- If unsure whether a button is only Save, stop and tell the user.

## Do Not Click

- Apply
- Easy Apply
- Submit
- Send
- Message
- Connect
- Follow
- profile edit buttons
- job alert setting buttons
- account setting buttons
- unsubscribe buttons
- report/block buttons
- any final action button unrelated to saving a job

Do not:

- apply to any job
- submit any form
- upload a resume or cover letter
- answer screening questions
- send messages
- connect with recruiters
- modify the user's LinkedIn profile
- change job alert settings
- follow companies
- change account settings
- bypass CAPTCHAs, rate limits, login checks, or access controls
- use aggressive or high-speed scraping behavior
- open or evaluate the saved-jobs tracker
- score, rank, or unsave jobs

## Expected Output

Produce a brief end-of-run summary with only:

- number of unique job cards recorded
- number of jobs reviewed
- number of duplicate cards skipped
- number of jobs saved
- number of jobs skipped
- uncertain jobs, with one short reason each
- any stop condition or LinkedIn access issue encountered
