# Experience Bank

> EXAMPLE FILE — fictional persona "John Doe". Run the `setup` skill to replace
> this with your own `experience_bank.md`. Reproduce the atom structure below for
> each of your real roles and projects.

- This file is the source of truth for detailed professional and personal-project experience used by the CV tailoring workflow. It captures what happened, the user's role, evidence strength, outputs, tools, methods, and factual limits.
- Do not add CV-writing instructions, agent behavior rules, or meta guidance here; those belong in `tailoring_skill.md`.
- Each "atom" is one coherent piece of evidence. Be specific and honest. The **Ground Truth Limits** section is what keeps generated CVs truthful — always fill it.

# Employer: Northwind Retail 2023.09-present

## Experience Atom: Self-Serve Sales Reporting Dashboards

Project family: Business Intelligence / Analytics
Project context: Junior data analyst on the commercial analytics team of a mid-size retailer. The team supported regional sales managers who relied on slow, manual spreadsheet reports.

### Situation

Regional managers received weekly sales numbers as hand-built Excel files, which were often late and inconsistent. The analyst was asked to help move recurring reporting into a self-serve BI dashboard so managers could answer their own questions.

### Stakeholders

- Regional sales managers (report consumers)
- Commercial analytics team lead
- Data engineering team (owned the warehouse tables)

### Personal Contribution

- Gathered reporting requirements from three regional managers and translated them into a metric list.
- Wrote SQL against the sales warehouse to build clean, documented base queries for revenue, units, and margin by region and category.
- Built a Power BI dashboard with filters for region, period, and product category.
- Defined consistent metric definitions (e.g. how returns affect net revenue) and documented them.
- Ran short walkthrough sessions to help managers adopt the dashboard.

### Outputs And Outcomes

- A Power BI dashboard replacing a recurring manual weekly report.
- Documented metric definitions adopted by the commercial team.
- Reduced the analyst team's weekly manual reporting time noticeably (qualitative; no formal measurement).

### Tools, Platforms, And Methods

- SQL
- Power BI
- Requirements gathering
- Metric definition and documentation

### Evidence Tags

Business intelligence; SQL; Power BI; dashboard design; stakeholder requirements; reporting automation; data storytelling; metric definition.

### Ground Truth Limits

The source evidence does not support claims that the user did any of the following:

- Built or owned the data warehouse or pipelines.
- Was the sole owner of the BI strategy.
- Built production data engineering infrastructure.
- Managed people.

## Experience Atom: Checkout Funnel A/B Test Analysis

Project family: Product / Growth Analytics
Project context: Supported the e-commerce team analyzing an experiment on a redesigned checkout page.

### Situation

The product team ran an A/B test on a new checkout layout and needed help deciding whether it improved conversion. The analyst supported the measurement and read-out.

### Stakeholders

- E-commerce product manager
- Analytics team lead

### Personal Contribution

- Pulled experiment event data with SQL and checked sample sizes and balance between variants.
- Calculated conversion rates per variant and a basic significance check.
- Built a short read-out summarizing the result and caveats (test duration, seasonality).
- Recommended extending the test before a final decision due to an inconclusive early result.

### Outputs And Outcomes

- A concise experiment read-out used in the product team's decision meeting.
- Recommendation to extend the test, which the team adopted.

### Tools, Platforms, And Methods

- SQL
- A/B testing concepts
- Conversion / funnel analysis
- Basic statistical significance testing

### Evidence Tags

Product analytics; experimentation; A/B testing; funnel analysis; SQL; data storytelling; decision support.

### Ground Truth Limits

The source evidence does not support claims that the user did any of the following:

- Designed the experimentation platform.
- Owned the product decision.
- Ran advanced causal inference or Bayesian experiment modelling.

# Employer: BrightMetrics Agency 2022.06-2022.08

## Experience Atom: Marketing Campaign Performance Reporting (Internship)

Project family: Marketing Analytics
Project context: Summer internship at a small digital marketing agency, supporting campaign performance reporting for several client accounts.

### Situation

Account managers needed regular performance summaries across paid channels for client reviews. The intern supported pulling and consolidating the data.

### Stakeholders

- Account managers
- Agency clients (indirectly, via reports)

### Personal Contribution

- Consolidated campaign metrics from multiple ad platforms into a single spreadsheet model.
- Built reusable templates for weekly client performance summaries.
- Wrote short plain-language commentary explaining changes for non-technical clients.

### Outputs And Outcomes

- Reusable reporting templates adopted for several client accounts.
- Weekly performance summaries delivered through the internship.

### Tools, Platforms, And Methods

- Excel / Google Sheets
- Campaign performance metrics (CTR, CPC, ROAS)
- Data consolidation and templating

### Evidence Tags

Marketing analytics; campaign reporting; data consolidation; stakeholder communication; spreadsheet modelling.

### Ground Truth Limits

The source evidence does not support claims that the user did any of the following:

- Owned media buying or budget decisions.
- Built automated data pipelines.
- Managed client relationships directly.

# Employer: Personal / self-directed - 2024

## Personal Project Atom: City Cycling Safety Data Explorer

Project family: Data Analysis / Visualization
Project context: Self-directed project analyzing open city cycling-accident data to practice end-to-end analysis and visualization.

### Situation

The user wanted a portfolio project demonstrating data cleaning, analysis, and clear visualization using a public open dataset.

### Personal Contribution

- Cleaned and combined several open municipal datasets with Python and pandas.
- Explored accident patterns by location, time of day, and weather.
- Built an interactive visualization highlighting higher-risk intersections.
- Wrote a short narrative summary of the findings.

### Outputs And Outcomes

- A documented notebook and an interactive visualization shared as a portfolio piece.

### Tools, Platforms, And Methods

- Python, pandas
- Data cleaning and exploratory analysis
- Data visualization

### Evidence Tags

Python; pandas; data cleaning; exploratory data analysis; data visualization; open data; portfolio project.

### Ground Truth Limits

The source evidence does not support claims that the user did any of the following:

- Built a production application.
- Deployed a hosted service at scale.
- Conducted peer-reviewed statistical research.
