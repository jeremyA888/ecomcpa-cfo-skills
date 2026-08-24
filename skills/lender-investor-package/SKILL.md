---
name: lender-investor-package
description: "Prepare ecommerce lender or investor packages with historicals, projections, uses, debt, covenants, collateral, and risks. Use financing-strategy to select funding and financial-reporting for routine reports."
license: MIT
---

# Lender and Investor Package

Prepare a traceable decision package without presenting assumptions as facts.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity and guarantor scope, reporting period and as-of date, currency and FX policy, accounting basis, close status, audience, amount and instrument under consideration, deadline, requested decision, and confidentiality level.

Choose one branch:

- **Lender:** underwriting, renewal, covenant, borrowing-base, or line-increase support. Center repayment capacity, liquidity, collateral, debt structure, and agreement-defined covenants.
- **Investor:** financing diligence or update tied to a capital decision. Center historical performance, operating drivers, forecast assumptions, use of proceeds, capitalization, risks, and milestones.
- **Board:** if no financing or covenant decision is involved, route to `financial-reporting`. Do not make one package serve all three audiences.

Use `thirteen-week-cash-flow` for weekly liquidity support, `cash-flow-forecast` for longer-range scenarios, and `financing-strategy` to compare instruments or decide whether to use cash before packaging a request.

## Evidence Gate

Create a source register with `document/input`, `source`, `extract date`, `covered period`, `entity/grain`, `coverage`, `close/audit status`, and limitation. Label each value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Keep historical actuals, forecast, and scenario separate. Tie statements and trailing-twelve-month schedules to closed trial balances or issued financial statements; tie cash to bank reconciliations, debt to signed agreements and lender statements, and inventory/receivables to reconciled subledgers. Identify management-prepared, unreviewed, reviewed, or audited material accurately.

Use user-defined materiality. If none is provided, report all reconciliation and forecast variances without silently setting a cutoff. If key periods, agreements, or control totals are missing, produce a readiness checklist and questions package rather than completing unsupported ratios or narrative claims.

## Audience-Specific Analysis

For a lender package, show:

- Sources and uses, primary repayment source, secondary support, and monthly or quarterly debt service.
- Debt schedule, maturity, rate, security, guarantees, availability, and covenant calculations exactly as defined in signed agreements.
- AR/AP aging, inventory quality and eligibility, collateral support, and borrowing-base inputs when requested.
- Base and downside liquidity with assumptions, including seasonality and inventory purchases.

For an investor package, show:

- Historical revenue, gross profit, explicitly defined contribution margin, operating income, cash flow, and working-capital trends.
- Forecast drivers and scenarios separately from actuals; never label a scenario as a forecast or commitment.
- Capitalization, use of proceeds, milestones, dependencies, and balanced risks.

For both branches, define `EBITDA = net income + interest + income taxes + depreciation + amortization`. Show adjusted EBITDA only with each adjustment and a reconciliation to reported net income. Do not calculate covenant ratios from a generic definition.

## Deliverable

Return a staged package containing:

1. Cover page with purpose, audience, confidentiality, scope, as-of date, basis, close/review status, and preparer.
2. Executive summary that distinguishes reported facts, calculated results, assumptions, scenarios, risks, and requested decision.
3. Historical statements and KPI schedules, forecast/scenario schedules, use-of-funds table, debt/covenant or capitalization schedules, and ecommerce inventory/channel exhibits appropriate to the branch.
4. Source register, reconciliation report, data-room index, open-item list, and likely diligence questions with evidence-backed answers or `unavailable`.

## Quality Gate

- Cross-foot every table and tie opening/closing balances and TTM amounts to controls.
- Confirm forecast statements are internally linked and use of funds matches the financing request.
- Confirm covenant names, formulas, periods, and thresholds match signed agreements.
- Confirm non-GAAP measures are clearly labeled and reconciled; no unsupported superlatives or performance claims appear.
- Confirm confidential, personal, bank, tax, payroll, and customer data is minimized and correctly permissioned.

## Guardrails

Stage drafts only. Never submit an application, upload a data room, contact a lender or investor, send or post materials, sign terms, move cash, pledge assets, or change access without explicit approval. Do not promise funding, valuation, covenant compliance, or future performance. Obtain qualified CPA/accounting review for financial presentation, lender review for agreement calculations, and legal or securities counsel review where an offering, solicitation, confidentiality obligation, or regulated disclosure requires it.
