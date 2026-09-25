---
name: pricing-profitability
description: "Model future ecommerce prices, discounts, promotions, bundles, subscriptions, shipping thresholds, surcharges and tests. Use product-margin for historical SKU economics and channel-profitability for allocation."
license: MIT
---

# Pricing Profitability

Translate a proposed commercial change into explicit unit, order, margin, cash, and test economics.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity, products/channels/markets, analysis period and as-of date, currency and FX policy, accounting basis, close status, current offer, proposed decision, approval owner, and effective/test window.

Choose the correct grain: SKU/unit, bundle, order/basket, subscription cohort, channel, or market. Route historical SKU cost reconstruction to `product-margin`, channel comparison to `channel-profitability`, and broad profit-leak review to `profit-improvement`.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `grain`, `coverage`, and limitation. Include prices, discounts, units/orders, refunds, landed COGS, fulfillment, outbound and customer-paid shipping, fees, return costs, and reliably attributable marketing. Label every value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate closed actuals, forecast, and scenario. Tie actual net revenue and COGS to financial controls and order/SKU detail to channel totals. Date competitor or marketplace evidence and treat it as context, not proof of customer response.

Use user-defined materiality; absent one, show every scenario delta. Unknown conversion, demand, churn, return, or mix response must be a labeled range or scenario, never a factual prediction. If baseline cost or transaction coverage is insufficient, deliver the data gaps and break-even requirements without recommending a rollout.

## Scenario Math

Define signs once: revenue and customer shipping are positive; discounts, refunds, COGS, and variable costs are displayed positive and subtracted.

- `net product revenue = gross product charges - discounts - product refunds/sales reversals`, excluding sales taxes and showing customer shipping revenue separately.
- `shipping contribution = customer shipping revenue - outbound shipping cost`.
- `contribution before marketing = net product revenue - recognized product COGS + shipping contribution - fulfillment - merchant/marketplace fees - expected return-processing, reverse-logistics, and write-off cost not already captured - other named variable costs`.
- `contribution after attributable marketing = contribution before marketing - reliably attributable incremental marketing`.
- `contribution % = contribution / (net product revenue + customer shipping revenue)` unless an approved company policy supplies another stated denominator; a zero or negative denominator is `not meaningful`.
- `required scenario orders = baseline total contribution / scenario contribution per order` when scenario contribution per order is positive.
- `break-even units = incremental fixed implementation cost / incremental contribution per unit` when incremental contribution is positive.

For free shipping, model basket distribution, weight/zone/service mix, customer shipping recovery, split shipments, and threshold migration at the order grain. For bundles, allocate price and discounts consistently and test the full basket, not isolated component margins. For subscriptions, show discount, churn assumption, fulfillment cadence, payment failure, and cohort contribution horizon.

Use user-approved base, downside, and upside response assumptions. A pricing experiment must define hypothesis, eligible population, control, duration or stopping logic, success metrics, margin/cash guardrails, and rollback decision; do not claim causality from an uncontrolled before/after comparison.

## Deliverable

Return:

1. Baseline and scenario tables with price, response assumptions, units/orders, net revenue, cost ladder, contribution, contribution %, cash timing, and variance.
2. Break-even requirements and sensitivity ranges, with every assumption and unavailable input visible.
3. Source register, reconciliation report, and data-quality limitations.
4. A staged experiment or rollout recommendation with owner, approvals, measurement plan, guardrails, and rollback trigger.

## Quality Gate

- Unit and order economics foot, and aggregate actuals tie to control totals.
- No cost is omitted or counted twice across product cost, landed additions, fulfillment, shipping, fees, returns, and marketing.
- Tax, shipping revenue, discounts, refunds, and bundles use consistent definitions.
- Scenario response is visibly an assumption, and actual, forecast, and scenario are not mixed.
- The proposed test can measure contribution and customer behavior without unsupported attribution claims.

## Guardrails

Stage analysis and test plans only. Never change prices, discounts, subscriptions, shipping rules, marketplace settings, ads, access, or live offers; never post, send, or move cash without approval. Do not invent elasticity, competitor prices, conversion lift, or customer behavior. Obtain qualified accounting/tax review for revenue and cost treatment and legal review for MAP, price-parity, competition, consumer, subscription, or marketplace obligations where applicable.
