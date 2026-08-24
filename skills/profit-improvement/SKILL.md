---
name: profit-improvement
description: "Diagnose ecommerce profit leaks and build an evidence-backed portfolio across price, COGS, freight, returns, ads, operations, payroll, and cash. Use for broad improvement; route detail to specialist skills."
license: MIT
---

# Profit Improvement

Prioritize improvements by verified economics, timing, confidence, dependencies, and risk—not generic percentages.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity, reporting period and as-of date, currency and FX policy, accounting basis, close status, baseline profit measure, cash horizon, constraints, decision owner, and decision to be made.

This is an orchestration skill. Route SKU economics to `product-margin`, price and promo scenarios to `pricing-profitability`, channel economics to `channel-profitability`, inventory accuracy to `inventory-cogs`, staffing to `staffing-plan`, structural cash release to `working-capital`, and weekly liquidity to `thirteen-week-cash-flow`. Preserve one baseline and prevent benefits from being counted in more than one workstream.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `entity/grain`, `coverage`, and limitation. Label values `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate closed actuals, forecast, and scenario. Tie the baseline P&L, balance sheet, and cash flow to closed controls; reconcile product/channel detail, spend vendors, payroll, inventory, and operational drivers before estimating impact.

Use user-defined materiality. Without one, show all identified variances or ask the user to choose a prioritization floor. If the baseline or driver evidence cannot support an estimate, label impact unavailable and return the measurement plan; never fabricate a savings range.

## Opportunity Model

Scan price/discounts, product and landed cost, returns, fulfillment/shipping, marketplace and merchant fees, marketing, software/agencies, payroll/capacity, inventory, payment timing, and financing cost.

For each lever show a calculation that can be audited:

- `run-rate profit effect = affected volume x verified unit effect`, or a fully specified spend change.
- `cash effect = incremental cash receipts + cash outflows avoided - incremental cash outflows - implementation cash cost`; do not call timing release profit.
- `net benefit = gross benefit - implementation cost - expected offset or leakage`.
- `confidence-weighted case = scenario benefit x explicitly stated probability` only if the user approves probability weighting; otherwise show scenarios separately.

Separate EBITDA/operating-profit effect from cash effect, one-time from recurring, and gross from net. Show ramp timing, owner, dependencies, reversibility, customer/control/compliance risk, and evidence confidence. Build a benefit bridge with one row per lever and a dependency/double-counting matrix.

## Deliverable

Return:

1. A baseline profit bridge and leak map tied to reported controls.
2. An opportunity register with formula, evidence, actual baseline, assumptions, scenario range, recurring/one-time profit and cash effects, cost, time-to-value, owner, dependencies, confidence, and risk.
3. A de-duplicated portfolio ranked by decision-useful net impact, confidence, timing, and constraints—not impact/effort alone.
4. Top actions with a named owner, first measurement, approval required, deadline, guardrail, and rollback condition.
5. Source register, reconciliation report, unavailable estimates, and next-data plan.

## Quality Gate

- Tie the starting profit and cash baselines to closed control totals.
- Reperform calculations and confirm all benefits are net of stated costs and offsets.
- Confirm no volume, cost, or benefit appears in two levers or specialist analyses.
- Confirm working-capital release is not mislabeled as profit and cost cuts do not silently assume unchanged demand or service.
- Confirm actual, forecast, and scenario are separate and every estimate is supported or visibly unavailable.

## Guardrails

Stage analysis and recommendations only. Never change prices, ads, vendors, software, staffing, payroll, purchasing, financing, access, or controls; never cancel, post/send, or move cash without approval. Do not recommend weakening compliance, accounting quality, security, customer experience, or critical controls merely to show savings. Obtain qualified accounting, tax, HR, legal, lender, or operational review where an action requires it.
