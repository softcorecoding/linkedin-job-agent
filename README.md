# LinkedIn Job Agent

A local-first LinkedIn job-search assistant for Codex.

This repo is not a standalone app and does not use the LinkedIn API. It is a set of Markdown skills that Codex reads to help you:

- shortlist LinkedIn jobs
- evaluate saved jobs against your real experience
- generate tailored CV PDFs for strong-fit roles

The browser stays visible, the workflow is human-in-the-loop, and the agent must not apply to jobs or take final actions for you.

## Requirements

- Codex app with the browser plugin available
- Python 3.8+
- `pip`
- `ripgrep` (`rg`)

The Codex CLI is not enough for this repo because the LinkedIn workflows require Codex's browser plugin.

The first `setup` run installs the Python PDF dependency from `tailor_cv/requirements.txt`. To install it yourself:

```bash
python3 -m pip install -r tailor_cv/requirements.txt
```

## First-Time Setup

Open this repo in Codex and say:

```text
setup
```

The setup skill interviews you and creates three git-ignored personal files:

- `job_shortlist/profile.md` - your candidate summary, hard exclusions, and shortlist signals
- `tailor_cv/experience_bank.md` - detailed evidence from your work, projects, tools, outcomes, and limits
- `tailor_cv/identity.json` - your name, contact line, languages, and education

The repo includes fictional examples in `sample/` so you can see the expected format. Your real personal files are ignored by git and should stay local.

## Normal Workflow

Use the commands in this order:

```text
linkedin
job <LinkedIn jobs search URL>
eval <LinkedIn saved jobs / job tracker URL>
cv <specific LinkedIn job URL>
```

You can also open the right LinkedIn page in Codex's visible browser first, then run the command without a URL:

```text
job
eval
cv
```

What each command does:

| Command | Purpose |
|---|---|
| `linkedin` | Opens LinkedIn in Codex's visible browser so you can log in or prepare the page. |
| `job` | Reviews a LinkedIn jobs search page, skips hard exclusions, checks job descriptions, and saves plausible jobs. |
| `eval` | Reviews saved jobs, scores them against your experience bank, and removes weak fits. |
| `cv` | Creates a tailored CV JSON and PDF for one specific job. |

For best results, start a fresh Codex session for each major step after setup.

## How Shortlisting Decides What To Save

The `job` skill reads `job_shortlist/profile.md` and saves only jobs that pass the save gate:

- the actual job description was opened and read
- no hard exclusion appears in the description
- profile-specific language exclusions were checked against the description and requirements
- the role connects to one or more candidate evidence anchors

If the job details cannot be read closely enough, the job is marked uncertain instead of being saved.

## CV Output

Tailored CVs are written under:

```text
tailor_cv/<company>_<role>/
```

Each output folder contains:

- the tailored CV JSON
- a PDF named from your identity, for example `john_doe_cv.pdf`

Generated CV folders are git-ignored.

## Safety Rules

The agent must not:

- submit applications
- click Apply, Easy Apply, Submit, Send, Message, Connect, or other final action buttons
- upload resumes or answer screening questions
- change your LinkedIn profile, account settings, alerts, or company follows
- bypass CAPTCHAs, rate limits, login checks, or security challenges
- use aggressive scraping behavior

You stay responsible for reviewing jobs, generated CVs, and any final application steps.

## Repository Layout

```text
.
├── AGENTS.md                       # routes commands to skills
├── README.md
├── linkedin.md                     # shared LinkedIn browser rules
├── linkedin_skill.md               # opens LinkedIn for login/session setup
├── setup_skill.md                  # creates personal source-of-truth files
├── sample/                         # fictional setup examples
│   ├── profile.example.md
│   ├── experience_bank.example.md
│   └── identity.example.json
├── job_shortlist/
│   └── shortlist_skill.md          # `job`
├── fit_evaluation/
│   └── fit_evaluation_skill.md     # `eval`
└── tailor_cv/
    ├── tailoring_skill.md          # `cv`
    ├── generate_tailored_pdfs.py
    ├── requirements.txt
    └── cv_structure.json           # tracked, identity-free CV structure
```

## Privacy Notes

The personal files below are git-ignored:

- `job_shortlist/profile.md`
- `tailor_cv/experience_bank.md`
- `tailor_cv/identity.json`
- generated `tailor_cv/<company>_<role>/` folders

Before sharing or committing changes, skim `git status` to make sure no personal data is staged.
