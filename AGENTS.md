# Project Instructions

This project is a personal, local-first LinkedIn job-search assistant. It is a set of agent "skills" that Codex (OpenAI's browser-capable coding agent) follows to shortlist jobs, evaluate fit, and tailor CVs. The shared browsing rules in `linkedin.md` target Codex's built-in browser tool.

Before using the job skills, the workspace must be set up and personalized. If `job_shortlist/profile.md`, `tailor_cv/experience_bank.md`, or `tailor_cv/identity.json` do not exist yet (only the `*.example.md` / `identity.example.json` versions are present), this is a fresh checkout: run the setup skill first. Its first step (`### 0. Set up the environment (first run)`) installs the runtime dependencies (`reportlab` plus a check for `ripgrep`), so run setup before the other skills even if you only need to install dependencies.

Use `setup_skill.md` when the user says "setup" (or when the required personal data files are missing).

Use `shortlist_skill.md` when the user says "job" followed by a LinkedIn jobs listing page, including pages where one job detail is open in the right-side panel.

Use `tailoring_skill.md` when the user says "cv" followed by a page of a specific LinkedIn job.

Use `fit_evaluation_skill.md` when the user says "eval" followed by a LinkedIn saved jobs / job tracker URL.

Whenever any cookie/privacy confirmation pop-up appears in the browser, always reject if available; if reject is not available then choose "only essential".

Whenever you open a url using the browser skill, make sure the browser is also visible to the user.

## Skills

You have the following skills to choose from:
`setup_skill.md` in the project root
`shortlist_skill.md` inside the "job_shortlist" directory
`tailoring_skill.md` inside the "tailor_cv" directory
`fit_evaluation_skill.md` inside the "fit_evaluation" directory

After choosing a skill, proceed to its .md file first, and follow the instructions in there.

## Source-Of-Truth Data Files

Skills read from these data files. Each skill states which ones it uses; this is the overview map:

- `job_shortlist/profile.md`: candidate summary, hard exclusions, and shortlist save signals.
- `tailor_cv/experience_bank.md`: detailed evidence atoms for CV tailoring and fit evaluation.
- `tailor_cv/identity.json`: the candidate's name, contact line, languages, and education, merged verbatim into each tailored CV.
- `tailor_cv/cv_structure.json`: identity-free output structure for the tailored-CV JSON.

`profile.md`, `experience_bank.md`, and `identity.json` contain personal data and are git-ignored. The repository ships `*.example.md` / `identity.example.json` with a fictional persona, plus the identity-free `cv_structure.json`, so the format is clear. The setup skill turns the examples into your real, git-ignored data files. Never write personal data into `cv_structure.json`; it stays tracked.

## Shared Rules

- `linkedin.md`: shared LinkedIn navigation rules (browser visibility, cadence, stop conditions, list pagination, completion across all pages) used by `shortlist_skill.md` and `fit_evaluation_skill.md`.
