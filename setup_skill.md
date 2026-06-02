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
| `tailor_cv/identity.json` | `tailor_cv/identity.example.json` |

`tailor_cv/cv_structure.json` is a generic, identity-free CV-structure template that stays tracked in the repo. Do not write the user's personal data into it; the user's name, contact, and education live in the git-ignored `tailor_cv/identity.json`.

If a target file already exists, ask the user whether to update it or leave it. Never overwrite real personal data without confirmation.

## Workflow

### 0. Set up the environment (first run)

Before personalizing, make sure the tools the skills depend on are installed. Do this once.

1. Confirm Python 3.8+ is available:

   ```bash
   python3 --version
   ```

2. Install the Python dependency for the CV generator:

   ```bash
   python3 -m pip install -r tailor_cv/requirements.txt
   ```

   If pip refuses on an externally-managed Python (PEP 668), create and activate a virtualenv, then re-run the install inside it:

   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   python3 -m pip install -r tailor_cv/requirements.txt
   ```

   (`.venv/` is git-ignored.)

3. Confirm `ripgrep` is available — the `cv` skill's banned-phrase audit uses it:

   ```bash
   rg --version
   ```

   If it is missing, install it (`brew install ripgrep` on macOS, or the system package manager) and tell the user if you cannot.

Note the `job`, `eval`, and `cv` skills also require Codex's built-in browser tool to be enabled, with the user already logged in to LinkedIn in that browser. You cannot install that here; just confirm with the user if browsing later fails.

### 1. Read the templates

Read all template files first so you understand the exact structure to reproduce:

- `job_shortlist/profile.example.md`
- `tailor_cv/experience_bank.example.md`
- `tailor_cv/identity.example.json`

(You may also glance at `tailor_cv/cv_structure.json` to see how identity and education are consumed, but you do not edit it during setup.)

Preserve their structure, headings, and section names. You are replacing the fictional persona's content with the user's, not redesigning the format.

### 2. Collect identity and education

Ask the user for:

- Full name
- City, country
- Email
- Phone (optional)
- LinkedIn URL (optional)
- Languages: each language with proficiency (e.g. `English (Fluent/C1), German (Intermediate/B1)`).
- Education: for each degree — institution, degree (e.g. MSc/BSc), field/specialization, years, GPA (optional), and optionally relevant coursework or thesis.

Create `tailor_cv/identity.json` from `tailor_cv/identity.example.json` and write:

- `candidate.name`
- `candidate.contact` — a single line: `City, Country | email | phone | linkedin`
- `languages` — a single comma-separated line of languages with proficiency.
- `education.entries` — one entry per degree, following the example's shape.

This file is git-ignored and holds the only personal identity data in the project. Do not put any of this into `tailor_cv/cv_structure.json`, which stays a tracked, identity-free template — the tailoring skill reads identity from `identity.json` and merges it into each per-job CV.

### 3. Build the experience bank

Build this **before** the profile — the profile's evidence anchors are derived from it.

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

### 4. Build the shortlist profile

Now write `job_shortlist/profile.md`, drawing on the experience bank you just built. Mirror the example's three sections:

- **Candidate Profile Summary** — a few sentences: career stage, target role families, the center of gravity of the roles they want. Ground this in the experience bank.
- **Candidate Evidence Anchors** — the themes/keywords that should make a job worth saving. **Derive these directly from the experience bank** (its Evidence Tags, tools, and outcomes), then confirm them with the user. Do not invent anchors the bank does not support.
- **Hard Exclusions** — layer these on top: companies, seniority ceilings, experience floor, excluded countries, role types, and any other automatic skip rules. Probe for these explicitly; users often forget exclusions until asked.

### 5. Confirm and finish

After writing the files, give the user a short summary:

- which files were created
- how many experience atoms were captured
- anything still thin or missing that they may want to expand later

Remind the user that these files are git-ignored and stay local, and that they can re-run "setup" anytime to extend the experience bank or update their profile.
