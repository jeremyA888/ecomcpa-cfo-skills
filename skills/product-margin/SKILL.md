---
name: product-margin
description: "Calculate historical ecommerce SKU, variant, bundle, or collection economics using a controlled revenue-to-contribution ladder. Use to rank products, diagnose cost drivers, or establish a pricing baseline. Use pricing-profitability for future price scenarios and inventory-cogs for reconciliation or cost-policy repair."
license: MIT
---

# Product Margin

Show which products contribute after traceable ecommerce costs without double counting landed cost.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity, product/channel/market scope, reporting period and as-of date, currency and FX policy, accounting basis and inventory-cost policy, close status, decision, and decision owner.

Choose SKU, variant, bundle, order, or collection grain. Route inventory reconciliation or capitalization-policy questions to `inventory-cogs`, future price/promo scenarios to `pricing-profitability`, and channel-level economics to `channel-profitability`.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `grain`, `coverage`, and limitation. Include units, sales, discounts, refunds, tax, shipping revenue, recognized COGS, landed-cost components, fulfillment, outbound shipping, fees, returns, warranty, and attributable marketing. Label every value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate actual, forecast, and scenario. Tie SKU/order net revenue to channel control totals and recognized COGS to the closed general ledger and inventory subledger. Report sales and cost coverage by SKU and value; do not calculate a portfolio margin from only the covered products without displaying excluded revenue.

Use user-defined materiality. Without it, show all SKU variances or allow an explicit filter. If net revenue, recognized cost, or unit mapping cannot be reconciled, mark the affected margin unavailable and produce the remediation needed; do not substitute current catalog cost for historical cost without labeling it as an assumption.

## Controlled Margin Ladder

Use one ladder and state signs. Revenue is positive; deductions and costs are displayed positive and subtracted.

1. `net product revenue = gross product sales - discounts - refunds/sales reversals`, excluding sales tax. Show customer shipping revenue separately.
2. `recognized product COGS` is one non-duplicated amount: base acquisition/manufacturing cost plus only landed additions included under the recorded inventory-cost policy. Do **not** subtract both product cost and a landed-cost total that already contains it.
3. `gross profit = net product revenue - recognized product COGS`; `gross margin % = gross profit / net product revenue`.
4. `shipping contribution = customer shipping revenue - outbound shipping cost`.
5. `contribution before marketing = gross profit + shipping contribution - fulfillment/pick-pack - merchant/marketplace fees - return processing/write-off not already captured - warranty - other named attributable variable costs`.
6. `contribution after attributable marketing = contribution before marketing - reliably attributable incremental marketing`.

Show both dollars and percent. Use net product revenue for product gross margin; absent an approved company policy, use net product revenue plus customer shipping revenue for contribution margin. State every denominator. Separate refunds from physical return processing, restocking, non-resalable write-off, and recovered inventory; avoid counting the same return loss in revenue, COGS, and return cost. Allocate shared costs only with a disclosed, decision-useful driver and show unallocated shared overhead separately.

If net product revenue is zero or negative, report margin percentages as `not meaningful` rather than forcing a rate.

## Deliverable

Return:

1. A ranked SKU/variant table with units, revenue ladder, cost ladder, gross profit, contribution before/after marketing, percentages, coverage, and value labels.
2. A bridge from control totals to analyzed products and a source/reconciliation report.
3. Driver analysis separating price, discount, mix, cost, freight, fulfillment, shipping, fee, and return effects.
4. A decision queue: scale, investigate, repair cost or offer, test, harvest, or consider exit—with quantified impact range, confidence, owner, and next evidence needed.

Before recommending liquidation or discontinuation, show inventory age, cash recovery, fixed-cost contribution, substitution, retention/halo role, contractual constraints, and downside scenario. Low margin alone is not sufficient.

## Quality Gate

- Cross-foot the ladder and tie net revenue, units, and COGS to control totals.
- Confirm product cost and landed cost are not double counted.
- Confirm shipping recovery, returns, bundles, fees, and marketing are treated consistently across SKUs.
- Confirm actual, forecast, and scenario remain separate and no unavailable input appears as zero.
- Confirm recommendations reflect evidence coverage and strategic dependencies, not rank alone.

## Guardrails

Stage analysis and recommendations only. Never change a price, product, bundle, supplier, inventory record, channel listing, ad allocation, access, or catalog; never liquidate/discontinue, post/send, or move cash without approval. Minimize customer-level data. Obtain qualified accounting/tax review for inventory and cost treatment and legal or contractual review before product, supplier, or marketplace actions where required.
