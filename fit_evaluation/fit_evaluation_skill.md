---
name: fit-evaluation
description: Evaluate saved LinkedIn jobs against the user's evidence bank, score actual fit, and unsave weak jobs.
---

## Goal

Review the user's LinkedIn saved jobs tracker and decide which saved jobs are actually worth applying.

This is the second workflow after shortlist:

- shortlist collects plausible jobs broadly
- fit evaluation performs the real evidence-based matching
- weak saved jobs should be removed
- strong or plausible jobs should remain saved for CV tailoring / application

## Required Files

- `tailor_cv/experience_bank.md`: primary evidence source for real experience, ownership level, useful angles, and claim boundaries.
- `job_shortlist/profile.md`: use only the Hard Exclusions section. Do not use shortlist anchors as scoring evidence.

## Fit Evaluation Standard

Be practical and honest. A job being saved does not mean it is a good fit.

For each job:

- read the full job description, especially the complete "About the job" section
- apply hard exclusions first
- build an internal requirement map from the role
- compare the role against `tailor_cv/experience_bank.md`
- judge whether the candidate has real, claim-safe evidence for the core requirements
- score the job from 1 to 5
- unsave jobs below 3

Do not expose the full internal evidence map. Use it to make the decision.

## Scoring Rubric

- `5`: Excellent fit. Core requirements are strongly supported by multiple evidence-bank atoms; role is close to the candidate's target direction.
- `4`: Strong fit. Most important requirements are supported; gaps are minor or manageable.
- `3`: Plausible fit. There is enough real evidence to justify keeping the job, but gaps, stretch, or uncertainty remain.
- `2`: Weak fit. Some superficial overlap exists, but core requirements are unsupported or not aligned enough.
- `1`: Not worth applying. Hard exclusion, wrong role family, severe evidence gap, or obvious mismatch.

Penalties and removals:

- Fall into one of the hard exclusions in `profile.md`
- Do not use company pages to infer employee count, sponsorship, or fit. You should be able to gather those information from the job post page itself.

## Evidence Bank Use

Treat `experience_bank.md` as a knowledge base.

For each job, identify:

- core role objective
- must-have responsibilities
- must-have skills or frameworks
- seniority and ownership expectations
- domain context
- strongest matching evidence atoms
- unsupported or risky requirements
- claim-boundary issues

Respect claim boundaries. Do not credit the candidate as role or role family unless the evidence bank directly supports that.

## LinkedIn Navigation

Start from the user-provided LinkedIn saved jobs / job tracker URL. Follow the shared rules in `linkedin.md` (browser visibility, cadence, stop conditions, list pagination, and completion across all pages). For fit evaluation, an "item" is a saved job.

Only inspect LinkedIn job-detail pages. The active page must be a job post URL such as `https://www.linkedin.com/jobs/view/<job-id>/...` and must contain the intended "About the job" section.

Do not intentionally navigate to or inspect:

- company pages
- company "Life" pages
- company "About" pages
- recruiter profiles
- people pages
- external company career pages
- Easy Apply flows
- external ATS pages

If LinkedIn accidentally redirects to a non-job page, immediately go back to the saved jobs tracker or reopen the original `/jobs/view/<job-id>/` URL. Treat the page as a navigation error, not as fit evidence.

Before scoring each job, verify that the job detail belongs to the intended saved-job card by confirming the title and company from the job page's visible text (the same text you read to evaluate the role). Do not rely on a page-title/document-title API for this; use the visible page text you already have.

## Completion Requirement

Follow Completion Across All Pages and the result-count gate in `linkedin.md`. "Handled" here means evaluated, and either kept or unsaved. Use the saved-job count shown by LinkedIn as the total for the gate.

Saved-job-specific note: unsaving a job removes it from the saved list, so the saved-job count and pagination shift as you work. Track each job by job ID in the Review Tracker so removed jobs are still counted as handled and are not re-evaluated, and re-read the current count rather than assuming the original total still holds.

## Review Tracker

Keep a compact internal tracker so saved jobs are not missed or evaluated twice. This list does not affect scoring.

Track only:

- job ID if visible in a `/jobs/view/<id>/` URL
- title
- company
- page/list position
- status: `pending`, `kept`, `unsaved`.
- score after evaluation, when applicable

Use job ID for de-duplication. If no ID is available, use title + company as fallback.

Do not show the full tracker to the user unless asked.

## Workflow

1. Read `tailor_cv/experience_bank.md`.
2. Read `job_shortlist/profile.md`, using only hard exclusions.
3. Open the saved jobs tracker URL and make the browser visible.
4. Work from top to bottom through the saved jobs list.
5. Add each visible saved job to the Review Tracker before opening details.
6. Open each pending saved job and verify the detail page matches the intended title and company.
7. Expand and read the full "About the job" section. Ignore company marketing text unless it is part of the role requirements or sponsorship/work-authorization language.
8. Apply hard exclusions first. If one applies, score `1` or `2`, unsave, and record the reason.
9. Build the internal requirement/evidence map against `experience_bank.md`.
10. Assign a 1-5 score using the scoring rubric and visible penalties.
11. If final score is below 3, unsave the job.
12. If final score is 3 or above, leave the job saved.
13. When the current page has no pending saved jobs, advance to the next page using List Pagination in `linkedin.md`. Continue through all saved-job pages until the Completion Requirement is met.

## Stop Conditions

Follow the shared Stop Conditions in `linkedin.md`. For this skill, "beyond the current skill's intended scope" means any action beyond saved-job evaluation and removal (e.g. apply, message, connect, submit, accept legal terms, alter profile/account settings).

## Expected Output

Produce a concise final summary:

- number of saved jobs evaluated
- number kept
- number unsaved
- number unavailable / duplicate / uncertain
- kept jobs ranked by score, with title, company, score, and brief evidence-based reason
- unsaved jobs with title, company, score, and brief reason
- uncertain jobs requiring human review, if any
- any LinkedIn access issue or stop condition encountered

End by telling the user the next workflow step exactly: start a new Codex session, pick one of the kept jobs, open its specific LinkedIn job post, and run `cv <specific LinkedIn job URL>` to generate a tailored CV for that role. Do not suggest applying, recruiter outreach, or profile changes unless the user explicitly asks.
