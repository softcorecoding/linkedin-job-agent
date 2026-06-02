---
name: setup
description: One-time personalization of the workspace. Interview the user and turn the shipped example files into their own git-ignored source-of-truth data files.
---

## Goal

Personalize this workspace for the current user by creating their own data files from the shipped examples. After setup, the job, eval, and cv skills will run against the user's real profile, experience, and identity.

This skill is conversational. Interview the user, then write files. Do not invent facts about the user — ask.

## Files this skill creates

| Target (git-ignored, personal) | From template |
|---|---|
| `job_shortlist/profile.md` | `job_shortlist/profile.example.md` |
| `tailor_cv/experience_bank.md` | `tailor_cv/experience_bank.example.md` |
| `tailor_cv/sample_structure.json` | already in repo with a fictional persona — edit in place to insert the user's identity + education |

If a target file already exists, ask the user whether to update it or leave it. Never overwrite real personal data without confirmation.

## Workflow

### 1. Read the templates

Read all three template files first so you understand the exact structure to reproduce:

- `job_shortlist/profile.example.md`
- `tailor_cv/experience_bank.example.md`
- `tailor_cv/sample_structure.json`

Preserve their structure, headings, and section names. You are replacing the fictional persona's content with the user's, not redesigning the format.

### 2. Collect identity and education

Ask the user for:

- Full name
- City, country
- Email
- Phone (optional)
- LinkedIn URL (optional)
- Education: for each degree — institution, degree (e.g. MSc/BSc), field/specialization, years, GPA (optional), and optionally relevant coursework or thesis.

Write these into `tailor_cv/sample_structure.json`:

- `candidate.name`
- `candidate.contact` — a single line: `City, Country | email | phone | linkedin`
- the Education section `entries` — one entry per degree, following the example's shape.

Leave every `[BRACKETED_PLACEHOLDER]` that represents dynamic, per-job CV content (profile summary, experience entries, skills) untouched. Those are filled per job by the tailoring skill, not during setup.

### 3. Build the shortlist profile

Interview the user to fill `job_shortlist/profile.md`, mirroring the example's three sections:

- **Candidate Profile Summary** — a few sentences: career stage, target role families, the center of gravity of the roles they want.
- **Hard Exclusions** — companies, seniority ceilings, experience floor, excluded countries, role types, and any other automatic skip rules. Probe for these explicitly; users often forget exclusions until asked.
- **Candidate Evidence Anchors** — the themes/keywords that should make a job worth saving. Derive these together with the user from their real experience.

### 4. Build the experience bank

This is the most important and most detailed file. Interview the user employer by employer, and project by project, to create `tailor_cv/experience_bank.md`. For each role or significant project, capture one or more "Experience Atoms" using the example's atom structure:

- a heading line: `# Employer: <name> <dates>` then `## Experience Atom: <name>` (or `## Personal Project Atom: <name>`)
- Project context
- Situation
- Stakeholders
- Personal Contribution
- Outputs And Outcomes
- Tools, Platforms, And Methods
- Evidence Tags
- **Ground Truth Limits** — what the evidence does NOT support claiming. Always fill this; it is what keeps generated CVs truthful.

Push for specifics: numbers, tools, scope, the user's actual personal contribution vs. the team's, and honest limits. Vague input here produces weak CVs later.

Work in passes if needed: capture the strongest 2-4 roles first, write the file, then offer to add more atoms.

### 5. Confirm and finish

After writing the files, give the user a short summary:

- which files were created
- how many experience atoms were captured
- anything still thin or missing that they may want to expand later

Remind the user that these files are git-ignored and stay local, and that they can re-run "setup" anytime to extend the experience bank or update their profile.
