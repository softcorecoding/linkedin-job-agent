---
name: setup
description: One-time personalization of the workspace. Interview the user and turn the shipped sample files into their own git-ignored source-of-truth data files.
---

## Goal

Personalize this workspace for the current user by creating their own data files from the shipped samples in `sample/`. After setup, the job, eval, and cv skills will run against the user's real profile, experience, and identity.

This skill is conversational. Interview the user, then write files. Do not invent facts about the user — ask.

## Files this skill creates

| Target (git-ignored, personal) | From template |
|---|---|
| `job_shortlist/profile.md` | `sample/profile.example.md` |
| `tailor_cv/experience_bank.md` | `sample/experience_bank.example.md` |
| `tailor_cv/identity.json` | `sample/identity.example.json` |

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

Read all sample files first so you understand the exact structure to reproduce:

- `sample/profile.example.md`
- `sample/experience_bank.example.md`
- `sample/identity.example.json`

(You may also glance at `tailor_cv/cv_structure.json` to see how identity and education are consumed, but you do not edit it during setup.)

Preserve their structure. You are replacing the fictional persona's content with the user's, not redesigning the format.

### 2. Collect identity and education

Ask the user for:

- Full name
- City, country
- Email
- Phone (optional)
- LinkedIn URL (optional)
- Languages: each language with proficiency (e.g. `English (Fluent/C1), German (Intermediate/B1)`).
- Education: for each degree — institution, degree (e.g. MSc/BSc), field/specialization, years, GPA (optional), and optionally relevant coursework or thesis.

Use the user provided information to create `tailor_cv/identity.json` from the structure example in `sample/identity.example.json`.

This file is git-ignored and holds the only personal identity data in the project. Do not put any of this into `tailor_cv/cv_structure.json`, which stays a tracked, identity-free template — the tailoring skill reads identity from `identity.json` and merges it into each per-job CV.

### 3. Build the experience bank

Build this **before** the profile — the profile's evidence anchors are derived from it.

This is the most important and most detailed file. Follow the `sample/experience_bank.example.md` structure, interview the user employer by employer, and project by project, to create `tailor_cv/experience_bank.md`. For each role or significant project, capture one or more "Experience Atoms" using the sample's atom structure:

If the user provides an existing CV, use it only as a starting source for draft atoms. A CV is usually too compressed to be a finished experience bank. Parse the CV into candidate roles, projects, tools, and outcomes, then run a follow-up interview before writing the final atoms.

Before accepting an atom as usable, check whether it has enough detail in these areas:

- the situation or business/research/problem context
- stakeholders or users of the work
- the user's personal contribution, separate from the team's contribution
- outputs, deliverables, and outcomes
- numbers, scale, frequency, or scope where honestly known
- tools, platforms, methods, and domain concepts
- evidence tags that can later support search and CV tailoring
- ground truth limits that prevent overclaiming

When details are missing, push for specifics: numbers, tools, scope, the user's actual personal contribution vs. the team's, and honest limits. Vague input here produces weak CVs later. Ask targeted questions such as:

- What did you personally build, change, analyze, decide, coordinate, or own?
- Who used the output, reviewed it, or depended on it?
- What tools, systems, data, models, frameworks, or processes were involved?
- What was the scale: users, customers, records, revenue, cost, time saved, volume, accuracy, turnaround time, frequency, or team size?
- What changed because of the work?
- What would be too strong or untrue to claim from this evidence?

Work in passes if needed: capture the strongest 2-4 roles first, write the file, then offer to add more atoms.

Before moving on to the profile, run a quality check on the draft experience bank. Count the atoms, identify any atom missing personal contribution, tools/methods, outcomes, or ground truth limits, and tell the user which atoms are still thin. If the bank is mostly one-sentence summaries, do not treat setup as complete; ask to deepen the highest-value 2-4 atoms first.

### 4. Build the shortlist profile

Now write `job_shortlist/profile.md`, drawing on the experience bank you just built to make "Candidate Profile Summary" and "Candidate Evidence Anchors" sections. Build "Hard Exclusions" section with the user. Mirror the sample's three sections:

- **Candidate Profile Summary** — a few sentences describing the candidate's career stage and evidence-backed role-family fit. **Derive this directly from the experience bank** (project families, role titles, evidence tags, tools, outcomes, and stakeholder context).
- **Candidate Evidence Anchors** — the themes/keywords that should make a job worth saving. **Derive these directly from the experience bank** (its Evidence Tags, tools, and outcomes), then confirm them with the user. Do not invent anchors the bank does not support.
- **Hard Exclusions** — guide the user through constraint-based skip rules only. Explain that a hard exclusion means "skip immediately even if the job otherwise looks good"; if the user is unsure, leave it out rather than turning a preference into a skip rule. Prompt with concrete categories: companies or sectors the user refuses, seniority ceilings or floor, excluded countries/cities/regions, relocation or commute limits, remote/hybrid/onsite constraints, role types to reject, language requirements, visa/sponsorship constraints, employment type (contract/freelance/internship/unpaid/commission-only), compensation floor if any, travel limits, and any other automatic skip rules. Keep these separate from evidence-derived fit signals.

Important boundary: `Candidate Profile Summary` and `Candidate Evidence Anchors` are evidence-derived. `Hard Exclusions` are user-supplied constraints. Do not ask users to provide target-role preferences as though they were a fourth profile section or an input to evidence anchors.

### 5. Confirm and finish

After writing the files, give the user a short summary:

- which files were created
- how many experience atoms were captured
- anything still thin or missing that they may want to expand later

Remind the user that these files are git-ignored and stay local, and that they can re-run "setup" anytime to extend the experience bank or update their profile.

Suggest that the user start a new Codex session before running the repo skills, so those workflows begin with the freshly created profile and experience files as their clean context. Tell them the next workflow step is `job <LinkedIn jobs search URL>` to shortlist plausible jobs.
