---
name: demand-planning
description: "Translate an ecommerce unit forecast into SKU replenishment, purchase timing, stockout/overstock risk, and inventory cash needs. Use for demand plans, reorder points, launch quantities, or PO timing. For historical inventory/COGS reconciliation use inventory-cogs; for event-wide planning use peak-season-planning."
license: MIT
---

# Demand Planning

Turn uncertain unit demand into explicit replenishment choices without false precision.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity, locations/channels/SKUs in scope, history cutoff and inventory as-of date, forecast horizon and time bucket, currency, accounting basis and close status, service-level or stock policy, and decision. Record the user's materiality/risk threshold; if absent, report every variance and risk without inventing one.

Route historical inventory valuation or GL/subledger differences to `inventory-cogs`, SKU economics to `product-margin`, strategic liquidity to `cash-flow-forecast`, and promotion/peak orchestration to `peak-season-planning`.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/location/SKU coverage`, `units and control total`, `tie-out status`, and `limitations`. Register historical shipped and returned units, usable on-hand, committed/backordered units, open POs with confirmed quantities/ETAs, lead-time history, MOQ/case packs, supplier capacity/terms, launches/promos, stock policy, and approved sales forecast.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Keep historical actuals, baseline forecast, and each scenario separate. If usable on-hand, open-PO status, lead time, or demand history is materially incomplete, return `Insufficient evidence`, a bounded risk view, and the decisions that cannot yet be supported.

## Planning Logic

- Choose a forecast method suited to available history and explain it. Do not infer seasonality, launch lift, cannibalization, or promo lift without evidence; label overrides as assumptions.
- Back-test where history allows. Show `bias = sum(forecast - actual) / sum(actual)` and `WAPE = sum(abs(forecast - actual)) / sum(abs(actual))`, with zero-denominator handling.
- Define `inventory position = usable on-hand + confirmed inbound - open allocations/backorders`. Make allocation and backorder categories mutually exclusive, and adjust transfers only once.
- Define `reorder point = expected demand during replenishment lead time + approved safety stock`. Safety stock must come from a user policy or a shown assumption; do not invent a service target.
- Define preliminary order quantity as `max(0, target inventory position - projected inventory position)`, then show MOQ, case-pack, capacity, shelf-life, and cash-term adjustments separately.
- Map deposits, final payments, freight, duties, and expected receipt dates into the cash plan. Keep unit flow and cash flow distinct.

## Deliverable

Return the decision frame and source register, forecast by SKU/time bucket with method and error/bias, inventory-position and reorder calculations, projected stockout/overstock windows, proposed order timing/quantity before and after constraints, cash schedule, scenario range, assumptions, and operations questions. Include unit control totals from SKU to category/company.

## Quality Gate

- Beginning units plus independently sourced movements tie to usable ending units or show a reconciliation.
- Actuals, baseline forecast, and scenarios remain separate; overrides retain owner, reason, and date.
- Recommended quantities show formulas, units, rounding, and constraints; no unavailable field becomes zero.
- Uncertain lead times or launch demand widen the presented range instead of producing a precise unsupported order.

## Guardrails

Stage demand plans and proposed orders as drafts only. Never create/approve a PO, change a forecast in a source system, commit supplier capacity, send a plan, move cash, or change access. Operations must validate availability and lead times; finance/accounting must review cash and capitalization implications where material.
