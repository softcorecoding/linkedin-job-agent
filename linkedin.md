# LinkedIn

Shared LinkedIn navigation rules for any skill that drives the browser over LinkedIn (`shortlist_skill.md`, `fit_evaluation_skill.md`, `tailoring_skill.md`). Skills reference this file instead of restating these rules.

Each skill defines what page or item it works on: a result card for shortlisting, a saved job for fit evaluation, or a specific job post for CV tailoring. The starting-page, visibility, and safety rules apply to all LinkedIn skills; pagination and completion rules apply to list workflows.

## Starting Page

If the user provided a LinkedIn URL, open that URL in the browser and make sure the browser is visible to the user before doing anything else.

If the user did not provide a URL, use the current visible Codex browser page as the starting page. Before continuing, verify from the visible page text or URL that it is the correct LinkedIn page type for the active skill:

- `job`: a LinkedIn jobs search/listing page, including a search page with a job detail open in the side panel
- `eval`: a LinkedIn saved jobs / job tracker page
- `cv`: a specific LinkedIn job post page, normally a `/jobs/view/<job-id>/` page

If the current page is not the right page type, stop and tell the user what page to open in the Codex browser, or ask them to rerun the command with the right URL.

## Browser Visibility

Make sure the browser is visible to the user before doing anything else.

## Reading The Page

To read or verify page content (titles, company, description, button labels, pagination), use the page's visible text or a screenshot — the methods the Codex browser runtime exposes cleanly. Prefer the visible text you have already read over taking an extra screenshot. Do not depend on a page-title/document-title API; it may not match the runtime and wastes a step on a failed call followed by the same fallback.

## Slow, Human-Like Cadence

- Prefer visible UI actions: scroll the current list, click one visible item, read the detail, decide.
- Avoid bulk opening, background tabs, parallel page loads, scraping loops, and rapid direct navigation across job IDs.
- Wait 2-3 seconds after opening an item before opening another.
- If navigation or loading fails, pause and inspect the visible page before trying one gentle recovery action.

## Saved Jobs Handoff

After shortlisting completes, the agent may offer a user-confirmed handoff into fit evaluation. If the user confirms, navigate using LinkedIn's visible UI:

1. Click the LinkedIn `Jobs` tab.
2. Click the `Job Tracker` tab.
3. Click `Saved`.
4. Verify that the Saved jobs / job tracker page is visible.
5. Continue with `fit_evaluation_skill.md` from that current page.

This handoff is allowed only after the shortlist summary has been produced and the user has confirmed. Do not use it to evaluate saved jobs during the shortlist workflow itself.

## Stop Conditions

Stop immediately if:

- LinkedIn shows HTTP 429, rate limiting, temporary restriction, login/security challenge, CAPTCHA, or suspicious activity warnings
- the browser leaves LinkedIn job pages and cannot safely return
- the UI changes in a way that makes the next action unsafe
- a click may trigger a final or unsafe action (apply, message, connect, submit, accept legal terms, alter profile/account settings) beyond the current skill's intended scope

When stopping early, summarize progress and explain which stop condition occurred.

## List Pagination (Codex browser tool)

LinkedIn lists (job search results, saved jobs) are split into numbered pages of about 25 items, not infinite scroll. The page controls sit at the very bottom of the list, below all lazy-loaded items, so they are not visible until the list is scrolled to the end.

Using the Codex browser tool:

1. Scroll inside the list area itself. On the job search page this is the left results column, which scrolls independently of the right-side detail panel and of the whole window. Move the pointer over the list before scrolling.
2. Scroll the list in steps, letting new items lazy-load, until it stops growing and the numbered pagination row (1, 2, 3 … Next) appears at the bottom. Confirm the pagination row from the page's visible text before judging that the list has ended; only take a screenshot if the visible text is unclear.
3. To advance, click the next numbered page button (or the Next / → control). Prefer clicking the visible page number over editing the URL.
4. After the new page loads, the list resets to the top with a fresh set of items. Record the new page/start offset in the tracker and handle its items from the top.
5. Repeat until the highest page number has been handled and no Next control remains.

Fallback only if the pagination row cannot be clicked reliably: adjust the `start=` parameter in the page URL in multiples of 25 (`&start=25`, `&start=50`, …). This is a list-paging fallback; it is not the same as editing `currentJobId`, which remains disallowed. Keep the slow cadence above.

## Completion Across All Pages

Do not stop after the first page, after an arbitrary number of items, or to ask whether to continue.

"Page" means one results page (about 25 items), selected by the numbered pagination control at the bottom of the list. Handling only the items currently visible in the viewport is NOT completion.

Continue until one of these is true:

- every item on every numbered page has been added to the tracker and handled, AND no higher-numbered page or Next control remains
- LinkedIn blocks access, rate limits, shows a security challenge, or hits another stop condition
- the user explicitly tells you to stop

### Result-count gate (hard requirement)

If LinkedIn shows a total count, treat it as a completion gate, not a soft check:

- Before ending, the count of unique handled items must approach the visible total, allowing only for duplicates, unavailable items, and LinkedIn loading inconsistencies.
- If handled items are well below the total (for example, ~25 handled out of 180), you are NOT done: advance to the next page and continue.
- If the tracker still has `pending` items, or any higher-numbered page exists, keep going regardless of how many items you have already handled.
- LinkedIn caps job search at about 1000 results (around 40 pages of 25). If the displayed total is larger, do not expect the handled count to reach it: the run is complete once the last reachable page has been handled and no higher-numbered page or Next control remains. Reaching the final available page always ends the run, even when the handled count is below the displayed total.

Do not treat "no next page" as true until you have scrolled the list all the way to the bottom and confirmed there is no higher page number and no Next control. LinkedIn only exposes partial chunks until the list is fully scrolled.
