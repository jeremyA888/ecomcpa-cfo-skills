---
name: kpi-dashboard
description: "Define governed ecommerce finance KPIs, formulas, source lineage, thresholds, and dashboard layouts. Use for KPI dictionaries or dashboard specifications. Use product-margin or channel-profitability for the underlying profitability analysis, and financial-reporting for period commentary."
license: MIT
---

# KPI Dashboard

Build a metric system that answers named decisions without hiding weak data.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record:

- Entity or consolidation scope, reporting period and as-of date, currency and FX policy, accounting basis, close status, decision audience, and decision to be made.
- Required comparison: prior period, budget, forecast, cohort, channel, product, or target.
- Routing: this skill governs definitions and layout. Use `product-margin`, `channel-profitability`, `working-capital`, or `thirteen-week-cash-flow` when those underlying analyses must be built; use `financial-reporting` for narrative reporting.

Do not invent targets. Use a user-approved target, covenant, budget, or historical baseline and identify its source.

## Evidence Gate

Create a source register with `metric/input`, `source`, `extract date`, `covered period`, `entity/grain`, and `coverage or limitation`. Label every value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Keep actual, forecast, and scenario values in separate columns. Tie revenue, COGS, inventory, cash, debt, and operating profit to the relevant closed financial statement or control total. Reconcile channel and operational sources to that control total before using them as authoritative.

If materiality is supplied, use it. Otherwise show all variances or let the user choose a filter; never silently create a threshold. If a KPI lacks a stable definition, adequate source coverage, or a reconciled denominator, mark it unavailable and provide the exact remediation step.

## Metric Definitions

For every metric state numerator, denominator, inclusions, exclusions, time basis, grain, attribution model, sign convention, and owner. Common formulas, subject to the recorded policy, are:

- `net product revenue = gross product sales - discounts - product refunds/sales reversals`, excluding sales taxes; show customer shipping revenue separately and disclose gift-card treatment.
- `product gross profit = net product revenue - recognized product COGS`; `product gross margin % = product gross profit / net product revenue`.
- `shipping contribution = customer shipping revenue - outbound shipping cost`.
- `contribution margin level N = product gross profit + shipping contribution - the explicitly listed variable costs for level N`; never use an unlabeled contribution margin. State its denominator; absent an approved policy, use net product revenue plus customer shipping revenue.
- `AOV = defined order-basis revenue / qualifying orders`; define cancellations, returns, tax, shipping, and zero-value orders.
- `CAC = acquisition spend / acquired customers` for a named attribution model and window.
- `MER = net revenue / total marketing spend`; `ROAS = attributed revenue / attributed ad spend`.
- `cohort LTV = cumulative cohort revenue, gross profit, or contribution / customers acquired in that cohort`; name the value basis and horizon.
- `repeat purchase rate = cohort customers with a qualifying repeat purchase / qualifying cohort customers` within a stated window.
- `inventory turns = recognized period COGS / average inventory`; disclose any annualization.
- `weeks of supply = saleable on-hand units / forecast weekly units`; show forecast version.
- `CCC = DIO + DSO - DPO`; show processor settlement lag separately unless already captured in DSO.
- `EBITDA = net income + interest + income taxes + depreciation + amortization`; label and reconcile adjustments separately.
- Calculate DSCR only from the signed agreement's definition. Without one, mark covenant DSCR unavailable rather than choosing a generic formula.

Ratios with a zero or negative denominator require an explicit `not meaningful` result, not a forced percentage.

## Deliverable

Return:

1. A KPI dictionary with formula, business meaning, source, cadence, owner, dimensions, target source, decision, status label, and quality note.
2. A dashboard layout ordered as outcome, drivers, risks, and required decisions, with actual/budget/forecast/scenario clearly distinguished.
3. A source register, reconciliation notes, unavailable-metric list, and remediation queue.
4. A short list of vanity, duplicative, or non-actionable metrics to omit.

## Quality Gate

- Recalculate sample rows and confirm totals tie to their controls.
- Confirm every displayed target and variance has a named source and period.
- Confirm metric names cannot mask different formulas across cards, periods, or channels.
- Confirm freshness and coverage are visible on the dashboard, not buried in notes.
- Confirm no unavailable value is rendered as zero and no actual is mixed with forecast or scenario.

## Guardrails

Stage specifications and draft calculations only. Never publish a dashboard, change source systems or access, send reports, move cash, or alter targets without approval. Treat payroll and customer-level data as sensitive and minimize or aggregate it. Obtain qualified accounting, legal, lender, or securities review when metric presentation or covenant reporting requires it.
