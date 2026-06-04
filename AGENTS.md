# Project Instructions

This project is a personal, local-first LinkedIn job-search assistant. It is a set of agent "skills" that Codex (OpenAI's browser-capable coding agent) follows to shortlist jobs, evaluate fit, and tailor CVs. The shared browsing rules in `linkedin.md` target Codex's built-in browser tool.

Precondition: This repository must be used from the Codex app with the browser plugin available. The Codex CLI will not work because it does not support the browser plugin required by the LinkedIn skills. If the current agent environment has no visible browser/browser plugin, tell the user to switch to the Codex app before running setup, linkedin, job, eval, or cv.

Before using the job skills, the workspace must be set up and personalized. If `job_shortlist/profile.md`, `tailor_cv/experience_bank.md`, or `tailor_cv/identity.json` do not exist yet (only the sample files in `sample/` are present), this is a fresh checkout: run the setup skill first. Its first step (`### 0. Set up the environment (first run)`) installs the runtime dependencies (`reportlab` plus a check for `ripgrep`), so run setup before the other skills even if you only need to install dependencies.

Use `setup_skill.md` when the user says "setup" (or when the required personal data files are missing).

Use `linkedin_skill.md` when the user says "linkedin" by itself or asks to open LinkedIn in the Codex browser so they can log in there.

Use `shortlist_skill.md` when the user says "job", either followed by a LinkedIn jobs listing page URL or with a LinkedIn jobs listing already open in the Codex browser, including pages where one job detail is open in the right-side panel.

Use `tailoring_skill.md` when the user says "cv", either followed by a specific LinkedIn job URL or with a specific LinkedIn job page already open in the Codex browser.

Use `fit_evaluation_skill.md` when the user says "eval", either followed by a LinkedIn saved jobs / job tracker URL or with the saved jobs / job tracker page already open in the Codex browser.

## Intended User Workflow

The designed workflow is:

1. `setup` to create the local profile, experience bank, and identity files.
2. Optional: `linkedin` to open LinkedIn in the Codex browser for login or session setup.
3. `job [LinkedIn jobs search URL]` to shortlist and save plausible jobs.
4. `eval [LinkedIn saved jobs / job tracker URL]` to score saved jobs and remove weak fits.
5. `cv [specific LinkedIn job URL]` to tailor a CV only for a kept, worthwhile job.

At the end of each skill, guide the user to the next step in this workflow and usually tell them to start a new Codex session for that next skill/workflow so it begins with clean context. Exception: after `job` finishes, the agent may ask whether the user wants to continue directly to `eval`; if the user confirms, navigate LinkedIn's visible UI to Jobs -> Job Tracker -> Saved, then proceed with `fit_evaluation_skill.md` from that Saved page. Do not suggest unrelated next steps such as applying manually, messaging recruiters, changing LinkedIn settings, broad career planning, or editing generated files unless the user explicitly asks. If the user starts in the middle of the workflow, complete the requested skill, then point them to the next canonical step.

Whenever any cookie/privacy confirmation pop-up appears in the browser, always reject if available; if reject is not available then choose "only essential".

Whenever you open a url using the browser skill, make sure the browser is also visible to the user.

## Skills

You have the following skills to choose from:
`setup_skill.md` in the project root
`linkedin_skill.md` in the project root
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

`profile.md`, `experience_bank.md`, and `identity.json` contain personal data and are git-ignored. The repository ships fictional sample setup files in `sample/`, plus the identity-free `tailor_cv/cv_structure.json`, so the format is clear. The setup skill turns the samples into your real, git-ignored data files. Never write personal data into `cv_structure.json`; it stays tracked.

## Shared Rules

- `linkedin.md`: shared LinkedIn navigation rules (browser visibility, cadence, stop conditions, list pagination, completion across all pages) used by `shortlist_skill.md` and `fit_evaluation_skill.md`.
