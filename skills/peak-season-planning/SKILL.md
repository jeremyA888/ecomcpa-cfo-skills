---
name: peak-season-planning
description: "Plan ecommerce Q4, BFCM, Prime Day, launches, or promotions across demand, inventory, pricing, cash, staffing, fulfillment, and daily controls. Use specialist skills for detailed component work."
license: MIT
---

# Peak Season Planning

Turn a seasonal plan into dated cash, inventory, capacity, margin, and decision controls.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity, event and channel scope, historical comparison period, planning horizon and as-of date, currency and FX policy, accounting basis, close status, event calendar, decision owner, and decisions required before each cutoff.

This is an orchestration skill. Use `demand-planning` for SKU replenishment, `pricing-profitability` for promo economics, `staffing-plan` for labor, `thirteen-week-cash-flow` for weekly liquidity, and `product-margin` or `channel-profitability` for baseline economics. Preserve one shared set of dates, scenario names, and financial definitions across them.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `entity/SKU/channel grain`, `coverage`, and limitation. Label values `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate historical actual, current actual, forecast, and scenario. Tie historical sales to channel reports and the general ledger, inventory to the reconciled subledger, open POs to approved supplier records, payroll to the staffing plan, and cash to the 13-week model. Record close status and late returns, chargebacks, fees, or freight bills that make the comparison incomplete.

Use user-defined materiality. Without it, show all plan-to-actual variances and let the user filter. If sales history, inventory availability, lead times, promo terms, fulfillment capacity, or cash timing is insufficient, issue a readiness gap list and decision deadlines instead of fabricating a complete plan.

## Integrated Plan

Build user-approved base, downside, and upside scenarios. Each scenario must state its own units, price/discount, return rate, ad spend, lead time, fulfillment capacity, and payout timing assumptions.

Use consistent formulas and signs:

- `net units available = saleable on hand + confirmed inbound before need date - committed units - safety stock`.
- `net product revenue = gross product sales - discounts - product refunds/sales reversals`, excluding sales taxes and showing customer shipping revenue separately.
- `shipping contribution = customer shipping revenue - outbound shipping cost`.
- `event contribution = net product revenue - recognized product COGS + shipping contribution - fulfillment - merchant/marketplace fees - return-processing/reverse-logistics/write-off costs not already captured - attributable event marketing`. State the percentage denominator; absent an approved policy, use net product revenue plus customer shipping revenue.
- `ending available cash = beginning available cash + receipts - disbursements + financing inflows - financing outflows`, with disbursements displayed positive and subtracted.
- `variance = actual - frozen plan`; report favorable/unfavorable only after defining what favorable means for that line.

Map PO deposits, final payments, freight, duties, payroll, ads, processor settlements, refunds, and credit-card due dates by week. Include post-event returns and chargebacks beyond the selling window.

## Deliverable

Return:

1. A scenario plan by week and channel covering units, net revenue, contribution, inventory, capacity, and cash.
2. A dated readiness checklist for inventory, pricing, ads, staffing, fulfillment, reporting, and cash.
3. A risk register with evidence, trigger, financial exposure, owner, mitigation, and latest safe action date.
4. A daily/weekly scorecard with frozen plan, actual, variance, source freshness, and escalation owner.
5. A post-season close plan for returns, fees, freight, inventory, cash, and lessons learned.

## Quality Gate

- Every specialist schedule uses the same event dates, scenarios, currency, and metric definitions.
- Unit, margin, inventory, and cash bridges foot and tie to their controls.
- No sales order, processor payout, inventory unit, or cost is double counted across channels or systems.
- Downside liquidity and capacity triggers occur early enough for an actionable response.
- Actual, forecast, and scenario remain visibly separate, and no unavailable input appears as zero.

## Guardrails

Stage plans and draft schedules only. Never launch a promotion, change a price or budget, place or cancel a PO, hire staff, change system access, send or post reports, borrow, or move cash without approval. Do not invent demand lift, conversion effects, carrier capacity, or financing availability. Obtain qualified accounting, legal, HR, lender, marketplace, or tax review where the proposed action requires it.
