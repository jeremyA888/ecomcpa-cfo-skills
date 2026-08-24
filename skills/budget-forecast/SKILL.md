---
name: budget-forecast
description: "Build ecommerce budgets, reforecasts, scenarios, and budget-versus-actual reviews. Use demand-planning for SKU purchasing, cash-flow-forecast for monthly cash, and thirteen-week-cash-flow for weekly cash."
license: MIT
---

# Budget and Forecast

Turn explicit operating drivers into a traceable plan that management can approve and measure.

## Establish the Decision Frame

- Read `.agents/ecom-finance.md` if it exists, then state the entity or consolidation scope, planning period and actuals cutoff/as-of date, currency, accounting basis and close status, model version, planning granularity, and decision to be made.
- Identify the approved baseline: prior budget, latest forecast, annual target, or none. Do not overwrite versions or blend baselines.
- Record the user's materiality threshold for variance review. If none is supplied, show every variance and rank by magnitude without labeling any immaterial.
- Route unit/SKU replenishment detail to `demand-planning`, headcount mechanics to `staffing-plan`, strategic monthly liquidity to `cash-flow-forecast`, and weekly liquidity to `thirteen-week-cash-flow`. Use `accounting-quality-audit` when source actuals are not decision-ready.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/entity coverage`, `control total`, `tie-out status`, and `limitations`. Register historical actuals, channel/SKU sales, approved price and promo plans, inventory/PO plan, payroll roster, contracts, debt schedule, tax-payment schedule, and management-approved drivers.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Separate actual, forecast, and each scenario in distinct columns or tables. If source actuals do not tie, or required drivers are unavailable, return the usable partial model plus `Insufficient evidence`, the blocked outputs, and the exact evidence needed.

## Model Structure

Use the company's documented metric policy. If it is absent, present a proposed definition for approval rather than asserting one:

- `gross product sales - discounts - product refunds/sales reversals = net product revenue`; exclude sales taxes and show customer shipping revenue separately.
- `net product revenue - inventory product cost recognized as COGS = product gross profit`.
- `shipping contribution = customer shipping revenue - outbound shipping cost`.
- `product gross profit + shipping contribution - other traceable variable selling costs = contribution margin`.

Do not count landed cost both inside product COGS and again below product gross profit. Keep merchant/marketplace fees, outbound fulfillment, and channel advertising out of product gross profit unless the user's established policy explicitly classifies them there; disclose any management-reporting reclassification. State the denominator for every margin percentage; absent an approved policy, use net product revenue for product gross margin and net product revenue plus customer shipping revenue for contribution margin.

Build driver formulas explicitly, such as `units x realized price = gross sales`, then model returns/discounts, product COGS, traceable variable costs, marketing, payroll, fixed operating expenses, inventory purchasing, working capital, taxes, debt principal and interest, distributions, and capex. State whether outflows/expenses are shown as positive deductions or signed negatives and use that convention consistently.

Integrate the P&L with balance-sheet and cash movements when the decision depends on liquidity. Do not imply a three-statement model if the evidence supports only an operating P&L.

For budget-versus-actual, show `variance = actual - budget` and `variance % = variance / abs(budget)` when the denominator is nonzero. Label favorable/unfavorable according to the line type, not the sign alone. Classify supported causes as timing, volume, rate/cost, mix, one-time, or accounting; label unsupported explanations as assumptions.

## Deliverable

Return the decision frame and source register, driver/assumption table, monthly or agreed-period plan, actual-versus-budget table, scenario comparison, cash/working-capital implications, and management decisions with owner and decision date. Show formulas, control totals, and unresolved evidence next to the affected lines.

## Quality Gate

- Historical actuals tie to the registered ledger/report or have an explicit reconciliation.
- Channel, product, and department detail sum to disclosed control totals; intercompany or elimination lines remain visible.
- Actual, forecast, and scenarios never share an unlabeled column, and an assumption is never presented as reported history.
- Scenario changes flow through all affected statements; no hard-coded balancing plugs or silent zeros are allowed.

## Guardrails

Stage budgets, forecasts, decisions, and proposed actions as drafts only. Never post entries, approve spend or hiring, place orders, send reports, move cash, or change system access. Tax, accounting-policy, covenant, and financing conclusions require review by the responsible qualified professional.
