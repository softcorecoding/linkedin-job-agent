---
name: tailoring-cv
description: Tailor the user's CV for a LinkedIn job using the experience bank as the main evidence source.
---

## Goal

Given a specific LinkedIn job, create a fresh, deeply tailored CV for that role.

The core idea is evidence-based tailoring:

- The job description defines what must be proven.
- `tailor_cv/experience_bank.md` contains the detailed evidence.
- The agent must search, interpret, and synthesize from the bank.
- The final CV must be dynamically written for the specific job, not assembled from repeated stock sentences.

## Employer-Facing Truth Standard

The CV must be truthful, but it should be an employer-facing version of the truth, not a raw project diary.

Use detailed evidence from the bank to understand what happened, then translate it into professional hiring signals. The evidence bank may contain raw facts for claim control, but final CV wording must elevate those facts into credible, concise, role-relevant impact.

For every bullet, ask:

- What hiring signal does this prove for this role?
- Is this detail externally meaningful to an employer, or only internally accurate?
- Can the same fact be framed at a higher professional level without exaggerating?
- Does the wording make the candidate look stronger, clearer, and more relevant while staying within ground-truth limits?

Avoid wording that is technically true but self-limiting, overly literal, overly operational, or focused on low-level artifacts rather than the professional value created. Do not let examples in the evidence bank become stock phrases; synthesize fresh wording for the target role.

## Required Files

- `tailor_cv/experience_bank.md`: primary evidence source for detailed professional and personal-project experience.
- `tailor_cv/generate_tailored_pdfs.py`: reusable PDF generator.
- `tailor_cv/cv_structure.json`: reference structure for job-specific JSON input.
- `tailor_cv/identity.json`: hardcoded source of truth for candidate identity (name/contact), education, and languages. The generator merges these in automatically — never write or edit them in the per-job JSON.

Do not read previously generated application folders or previous tailored CV JSON/PDF files as source material. They can create bias and repeated phrasing. Use only the files listed above plus the live job description.

## Outputs

The generator writes all application documents into `tailor_cv/[slug]/`, a folder it creates from the JSON's `output_base` (a `[company_name]_[job_title]` slug). You do not create this folder — you only write the tailoring JSON (Step 7). Inside, the generator produces:

- `[slug].json` — a staged copy of your tailoring JSON
- `[your_name]_cv.pdf` — named automatically by slugifying `candidate.name` from `identity.json` (e.g. `john_doe_cv.pdf`); you do not set it.

## Core Workflow

### 1. Open And Analyze The Job

Start the browser with the user-provided LinkedIn job URL. Do not ask for permission to open it.

Make sure the browser is visible to the user.

On the LinkedIn post:

- Make sure to expand the full "About the job" section.
- Read the full job description carefully.
- Ignore company marketing text unless it affects the role requirements.

### 2. Build A Job Requirement Map

Before reading user sources deeply, convert the job into an internal requirement map.

Identify:

- role objective and business context
- must-have responsibilities
- must-have skills
- preferred skills
- seniority and ownership expectations
- domain/industry context
- tools, frameworks, platforms, and keywords
- implicit hiring criteria

Do not write the CV yet.

### 3. Read User Sources

Read:

- `tailor_cv/experience_bank.md`
- `tailor_cv/cv_structure.json`

Use the source hierarchy this way:

- `experience_bank.md` is the primary source for the user's actual experience: what the user did at work, what the user built or contributed to in personal projects, project details, ownership level, tools, outcomes, and ground-truth limits.
- `cv_structure.json` is for output formatting only.
- `identity.json` holds the candidate's hardcoded identity, education, and languages. In `cv_structure.json` these appear as `[INJECTED_FROM_IDENTITY_JSON]` placeholders (the `candidate` block, the Education section, and the `Languages` skills line) so you can see where they sit in the final CV. Leave those placeholders untouched — the generator overwrites them from `identity.json` at render time. Do not fill, tailor, or invent values for them.

### 4. Search The Experience Bank For Evidence

Treat the experience bank as a knowledge base, not as a text snippet library.

For each major job requirement, search the full experience bank for relevant evidence atoms. Consider direct and adjacent evidence.

Create an internal evidence map:

- job requirement
- strongest matching experience atom(s)
- usable facts
- ground-truth limits
- how the evidence should be reframed for this specific role

Do not expose the full evidence map in the final documents. Use it to reason.

Derive role-specific writing angles during this step. Do not expect the bank to provide "strong CV angles"; instead infer them from the situation, stakeholders, personal contribution, outputs, tools, evidence tags, and ground-truth limits. A good writing angle is a job-relevant interpretation of real evidence, not a reusable label copied from the bank.

### 5. Suitability Decision

Judge whether tailoring is worthwhile after mapping the job to the evidence bank.

Give an internal rating:

- `1`: weak fit; major job requirements are unsupported.
- `2`: viable fit; enough relevant evidence exists, but there are some gaps or careful positioning is needed.
- `3`: strong fit; the experience bank contains clear, role-relevant evidence across most core requirements.

These suitability labels are internal decision language only. Never copy rating words or evaluative suitability phrases into the employer-facing CV, including the profile summary, title, section headings, bullets, skills, JSON, or PDF.

If rating is `1`, stop before generating documents. Tell the user the main gap or hard concern and ask whether they still want to proceed.

If rating is `2` or `3`, continue generating the tailored CV unless the user explicitly asked only for evaluation.

### 6. Design The CV Strategy

Before writing the JSON, decide the CV strategy.

This strategy should answer:

- What is the role-specific story of this CV?
- Which 3-5 experience atoms are most relevant?
- Which experience atoms should be omitted because they distract from the target role?
- Which parts of professional experience, and personal project experience should be foregrounded?
- Which skills categories should appear for this job?
- What wording should be careful because of ground-truth limits?
- What role-specific writing angles should be derived from the factual evidence?

The CV structure may change per job. Do not force every generated CV to have the same bullets, same order, same section emphasis, or same phrasing.

### 7. Write A Fresh Tailored CV

Create a full tailored CV for the specific job using `cv_structure.json`.

The structure JSON is a structural template, not a fixed-length template. You write the tailored parts only: subtitle, profile summary, experience, and the role-relevant skill categories. The name/contact, education, and `Languages` line stay as their `[INJECTED_FROM_IDENTITY_JSON]` placeholders — they are merged in from `identity.json` at render time, so do not write or alter them. Dynamically add, remove, reorder, or resize experience entries, subsections, and bullet counts based on the job. Do not treat placeholder counts as required output counts.

All projects/experiences under the same employer should appear as one employer entry with multiple themed subsections.

The final CV must be concise enough to fit within a maximum of 2 pages.

Rules for dynamic synthesis:

- Write from scratch for this job.
- Do not copy-paste sentences from `experience_bank.md`, previous CVs, or prior generated outputs.
- Facts, numbers, tools, and project details may be reused, but the wording must be newly synthesized according to the job.
- Use the job description's language naturally where it matches real evidence.
- Reorder, condense, expand, or omit experience based on the job's actual requirements.
- Combine evidence across multiple atoms when useful.
- translate raw facts into cv suitable language.
- Avoid evaluative fit-language in all employer-facing CV content. Banned examples include "strong fit", "ideal candidate", "perfect match", "uniquely positioned", "good fit", "great fit", "excellent fit", "well suited", and "best suited".
- Do not describe the candidate's suitability directly. Instead, describe the candidate's actual experience, responsibilities, tools, outcomes, and transferable evidence.

Write this tailored CV to a single working JSON file before auditing it — for example `/tmp/[slug].json`, where `[slug]` is a `[company_name]_[job_title]` slug using only letters, digits, and underscores. Set the JSON's `output_base` field to that same `[slug]`.

Do not create any folder under `tailor_cv/` yourself. The generator (Step 9) is what creates the output folder: it reads `output_base`, makes `tailor_cv/[slug]/`, copies this JSON into it, and writes the PDF there. The Step 8 audit runs against the working JSON file you just wrote.

### 8. Claim And Originality Audit

Before generating PDFs, audit the tailored CV.

Check:

- every bullet supports this specific application
- every claim respects the relevant atom's `Ground Truth Limits`
- no copied bank sentence appears as a final CV bullet unless there is no reasonable alternative
- no repeated template sentence used across unrelated roles
- profile, skills, and experience framing are deeply tailored to the job
- final bullets are employer-facing and do not expose low-signal internal mechanics from the evidence bank
- no internal reasoning, evidence map, audit notes, or hidden comments appear in the final JSON or PDF
- no internal suitability-rating language or evaluative fit-language appears anywhere in the JSON. Search explicitly for banned phrases before generating the PDF:

```bash
rg -i "strong fit|ideal candidate|perfect match|uniquely positioned|good fit|great fit|excellent fit|well suited|best suited" /tmp/[slug].json
```

The command must return no matches. If it finds anything, revise the JSON and repeat the search before generating the PDF.

Fail closed: if any check fails, revise before generating PDFs.

### 9. Generate PDFs

Run the reusable generator on the working JSON file from Step 7. Do not create the output folder yourself and do not write a new rendering script per job — the generator creates `tailor_cv/[slug]/` from `output_base`, copies the JSON into it, and writes the PDF there, printing both final paths when it finishes.

The generator depends on `reportlab`. If it is not installed (an `ImportError` for `reportlab` when running the generator), install it once into the same interpreter:

```bash
python3 -m pip install reportlab
```

Then run the generator:

```bash
python3 tailor_cv/generate_tailored_pdfs.py /tmp/[slug].json
```

PDFs must be clean, professional, readable, ATS-friendly, human-friendly, and submission-ready.

The generator renders the JSON strings verbatim (it only escapes and wraps them, never rewrites words), so the PDF cannot contain any phrase that is not already in the JSON. The JSON banned-phrase search from the Claim And Originality Audit is therefore authoritative — do not re-extract or re-read the generated PDF to re-check for banned language. Just confirm that JSON search returned no matches before considering the PDF final.

### 10. Final User Summary

After generating the PDF, tell the user briefly:

- the suitability rating
- the main experience evidence used
- any careful positioning or gaps
- the generated file path

Do not dump the full internal evidence map unless the user asks.

End by telling the user that the designed workflow for this job is complete: they should review the generated PDF themselves before using it. If they want another tailored CV, the next canonical step is to start a new Codex session and run `cv <specific LinkedIn job URL>` for another kept job from fit evaluation. Do not suggest applying, messaging recruiters, changing LinkedIn settings, or additional career-planning steps unless the user explicitly asks.
