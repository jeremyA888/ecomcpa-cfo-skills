---
name: channel-profitability
description: "Analyze ecommerce contribution by channel, marketplace, geography, segment, or fulfillment path. Use product-margin for SKUs, inventory-cogs for inventory accounting, and profit-improvement for broad action."
license: MIT
---

# Channel Profitability

Show what each channel contributes without hiding attribution limits or forcing shared costs into arbitrary precision.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity/consolidation scope, period and as-of date, currency, accounting basis and close status, channel dimension, decision, and the company's approved gross/contribution-margin definitions. Record user-defined materiality; if absent, report every variance without silently choosing a threshold.

Route product/SKU contribution work to `product-margin`, historical inventory valuation and reconciliation to `inventory-cogs`, customer-level cohort economics to an appropriate customer-analytics workflow, and enterprise-wide opportunity prioritization to `profit-improvement`.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/entity/channel coverage`, `control total`, `tie-out status`, and `limitations`. Register channel orders, returns/discounts/chargebacks, settlements, GL revenue and COGS, inventory cost, merchant/marketplace fees, fulfillment/shipping, traceable advertising, and any support-cost driver.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Separate actual, forecast, and scenario economics. If channel totals cannot reconcile to the ledger/settlement universe or product cost is unavailable, return `Insufficient evidence`, the partial view, and the decisions that remain unsupported.

## Contribution Model

Use the company's documented policy. If absent, present a definition for approval:

`gross product sales - discounts - product refunds/sales reversals/chargebacks = net product revenue`

Exclude sales tax and other amounts collected on behalf of authorities. Show customer shipping revenue separately.

`net product revenue - inventory product COGS = product gross profit`

`shipping contribution = customer shipping revenue - traceable outbound shipping`

`product gross profit + shipping contribution - traceable merchant/marketplace fees - traceable fulfillment - traceable channel advertising - other approved variable costs = contribution margin`

State whether costs are positive deductions or signed negatives. Landed cost belongs inside product COGS when already capitalized there; never deduct it again. Separate directly traceable costs, defensible allocations, and unallocated shared overhead. Show allocation driver and formula; do not allocate shared cost merely to make channel profit sum to company net income.

Align sales and returns to a disclosed order, shipment, or accounting-period convention. Expose settlement timing, mixed fulfillment, cross-channel promotions, ad-attribution windows, transfer pricing/intercompany effects, and working-capital differences. Label causal explanations without evidence as assumptions.

## Deliverable

Return the decision frame and source register, channel waterfall with amount and margin percent, total-company reconciliation, traceable/allocated/unallocated cost view, confidence by material line, key drivers, data gaps, and draft channel decisions. State every percentage denominator; absent an approved policy, use net product revenue for product gross margin and net product revenue plus customer shipping revenue for contribution margin. A zero or negative denominator is `not meaningful`.

## Quality Gate

- Channel columns sum to the disclosed sales/ledger universe or include explicit unassigned and reconciling columns.
- Product COGS and landed cost are counted once; returns, discounts, fees, and ad costs use consistent periods.
- Actual, forecast, and scenarios are separate, and reported values are not mixed with allocations without labels.
- Confidence follows source quality and reconciliation coverage, not narrative certainty.

## Guardrails

Stage the analysis and recommendations as drafts only. Never change prices, channel settings, budgets, allocations in the ledger, send reports, move cash, or change access. Accounting-policy, transfer-pricing, tax, and material allocation decisions require review by the responsible qualified professionals.
