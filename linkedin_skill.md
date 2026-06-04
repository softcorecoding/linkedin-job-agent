---
name: linkedin
description: Open LinkedIn in the visible Codex browser so the user can log in or prepare LinkedIn before running the job-search workflows.
---

## Goal

Open LinkedIn in Codex's visible browser and hand control to the user so they can log in, confirm their session, or navigate to the LinkedIn page they want to use next.

This is a handoff workflow, not an automation workflow. Do not inspect jobs, save jobs, evaluate fit, tailor a CV, scrape pages, or continue into another skill unless the user explicitly starts that workflow afterward.

## Workflow

1. Open `https://www.linkedin.com/` in the browser.
2. Make sure the browser is visible to the user.
3. If a cookie/privacy confirmation appears, reject if available; if reject is not available, choose only essential.
4. If LinkedIn shows a login page, stop and tell the user to complete login in the visible browser.
5. If LinkedIn is already logged in, stop and tell the user LinkedIn is open in the Codex browser.

## Boundaries

Do not:

- enter credentials, one-time codes, CAPTCHA text, or security answers
- bypass login, CAPTCHA, rate limits, access controls, or security checks
- change account, privacy, notification, job alert, or profile settings
- click Apply, Easy Apply, Submit, Send, Message, Connect, Follow, or any other final action
- browse job listings or job details as part of this handoff

## Expected Output

Keep the response brief. Tell the user LinkedIn is open in the Codex browser, then point them back to the canonical workflow. If they navigate to the relevant LinkedIn page in this same browser, they may run the next command without pasting the URL:

- `job` after they have a jobs search page ready, or `job <LinkedIn jobs search URL>`
- `eval` after they have the saved jobs / job tracker page ready, or `eval <LinkedIn saved jobs / job tracker URL>`
- `cv` after they have a specific kept job post ready, or `cv <specific LinkedIn job URL>`

If the user needed to log in, tell them to finish login in the visible browser first.
