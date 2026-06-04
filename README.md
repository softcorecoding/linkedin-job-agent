# LinkedIn Job Agent

A local-first, human-in-the-loop assistant for job hunting on LinkedIn. It's a set of **agent skills** — Markdown instruction files that [Codex](https://openai.com/codex/), OpenAI's coding agent, reads and follows to help you search, evaluate, and apply for jobs more efficiently. The browsing rules target Codex's built-in browser tool specifically.

There is no app to install and no LinkedIn API. The agent drives a visible browser, slowly and carefully, the way you would. You stay in control: it never submits applications or takes unsafe actions on your behalf.

## What it does

The agent has three skills, each triggered by a keyword plus a LinkedIn URL:

| Say | …followed by | What happens |
|---|---|---|
| **`job`** | a LinkedIn job-search results URL | First-pass **shortlisting**: scans every result page, skips your hard exclusions, and saves plausibly relevant jobs for later. |
| **`eval`** | your LinkedIn saved-jobs URL | **Fit evaluation**: re-reads each saved job, scores it 1-5 against your real experience, and unsaves the weak ones. |
| **`cv`** | a specific LinkedIn job URL | **CV tailoring**: writes a fresh, evidence-based CV for that role and generates a clean PDF. |

A fourth skill, **`setup`**, personalizes the workspace for you the first time (see below).

The workflow is intentionally a funnel: `job` casts a wide net → `eval` sharpens it → `cv` invests effort only in the roles worth it.

## How it works

- `AGENTS.md` is the router. Codex reads it and dispatches to the right skill based on your keyword.
- Each skill is a `*_skill.md` file with detailed, safety-conscious instructions.
- `linkedin.md` holds shared browsing rules (slow human-like cadence, pagination, stop conditions, never trigger unsafe actions).
- Your personal data lives in a few **source-of-truth files** that the skills read:
  - `job_shortlist/profile.md` — your target roles, hard exclusions, and save signals.
  - `tailor_cv/experience_bank.md` — your detailed, honest experience, used as evidence for CVs.
  - `tailor_cv/identity.json` — your name, contact, languages, and education (fixed personal facts merged into every CV).
  - `tailor_cv/cv_structure.json` — the identity-free CV output structure (a generic template, not personal data).
- `tailor_cv/generate_tailored_pdfs.py` renders a tailored CV JSON into a polished, ATS-friendly PDF.

## Prerequisites

Before setup, make sure these are available:

| Dependency | Why it's needed | Notes |
|---|---|---|
| **Codex app** with its **built-in browser tool enabled** | Drives LinkedIn for the `job`, `eval`, and `cv` skills | The Codex CLI will not work for this repo because it does not support the browser plugin. A LinkedIn account must already be logged in inside the app browser; the agent does not handle login. |
| **Python 3.8+** | Runs the CV PDF generator | `python3 --version` to check. |
| **pip** | Installs the Python dependency below | Ships with Python; on PEP-668 ("externally-managed") systems, use a virtualenv or `pip install --user` if a plain install is refused. |
| **reportlab** (Python package) | The only third-party Python library; renders the CV PDF | Installed via `requirements.txt` in setup step 2. |
| **ripgrep (`rg`)** | The `cv` skill's banned-phrase audit greps the generated JSON | `rg --version` to check. Install via `brew install ripgrep` (macOS) or your package manager. |

## Setup

### 1. Get the files into your agent

Clone or download this repo, then open the folder with Codex. The agent should pick up `AGENTS.md` automatically.

### 2. Install the PDF dependency

The `setup` skill (step 3) installs this for you on its first run, so you can normally skip this step. To install manually instead, the CV generator needs `reportlab` (the only third-party Python package):

```bash
python3 -m pip install -r tailor_cv/requirements.txt
```

If pip refuses on an externally-managed Python, create a virtualenv first (`python3 -m venv .venv && source .venv/bin/activate`) — `.venv/` is already git-ignored.

### 3. Personalize the workspace

This repo ships with a **fictional sample persona ("John Doe")** in `sample/` so you can see the expected format. Replace it with your own data by telling your agent:

```
setup
```

The `setup` skill interviews you and writes your own files:

- `job_shortlist/profile.md` (from `sample/profile.example.md`)
- `tailor_cv/experience_bank.md` (from `sample/experience_bank.example.md`)
- `tailor_cv/identity.json` (from `sample/identity.example.json`) — your name, contact, languages, and education

All three personal files are **git-ignored**, so they stay on your machine and never get committed.

You can copy the sample files from `sample/` to their real target paths and fill them in by hand instead — `setup` just makes it conversational. Re-run `setup` anytime to extend your experience bank or update your profile.

## Usage

Once personalized, just talk to your agent with a keyword and a URL:

```
job   https://www.linkedin.com/jobs/search/?keywords=data%20analyst&...
eval  https://www.linkedin.com/my-items/saved-jobs/
cv    https://www.linkedin.com/jobs/view/1234567890/
```

Tailored CVs are written to `tailor_cv/<Company>_<Role>/` as a JSON + a PDF named from your name (e.g. `john_doe_cv.pdf`). These output folders are git-ignored.

## Safety model

This assistant is deliberately conservative:

- The browser stays **visible** to you the whole time.
- It uses a **slow, human-like cadence** — no scraping loops, no bulk tab opening, no rapid job-ID navigation.
- It **stops immediately** on rate limits, CAPTCHAs, login/security challenges, or any unsafe UI state.
- The `cv` skill respects **ground-truth limits** in your experience bank, so it tailors aggressively but does not fabricate claims.
- It will **never** submit an application, send a message, connect with a recruiter, change your profile, or click any final/unsafe action.

You remain responsible for reviewing everything and for complying with LinkedIn's Terms of Service.

## Repository layout

```
.
├── AGENTS.md                       # router: maps keywords to skills
├── README.md
├── linkedin.md                     # shared LinkedIn browsing rules
├── setup_skill.md                  # one-time personalization
├── sample/                         # fictional setup samples
│   ├── profile.example.md          # → job_shortlist/profile.md
│   ├── identity.example.json       # → tailor_cv/identity.json
│   └── experience_bank.example.md  # → tailor_cv/experience_bank.md
├── job_shortlist/
│   └── shortlist_skill.md
├── fit_evaluation/
│   └── fit_evaluation_skill.md
└── tailor_cv/
    ├── tailoring_skill.md
    ├── generate_tailored_pdfs.py   # JSON → PDF
    ├── requirements.txt
    └── cv_structure.json           # identity-free CV output structure
```

## Notes for sharing

- All three personal data files (`profile.md`, `experience_bank.md`, `identity.json`) are git-ignored, so your identity, experience, and target roles never get committed. The tracked `sample/` files hold only the fictional sample persona.
- It's still good practice to skim `git status` before your first commit to confirm nothing personal is staged.
