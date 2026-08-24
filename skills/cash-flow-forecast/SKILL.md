---
name: cash-flow-forecast
description: "Build or review a strategic monthly ecommerce cash forecast across inventory, payroll, debt, advertising, launches, and growth. Use for medium-term liquidity and runway. For tactical weekly cash use thirteen-week-cash-flow; for an integrated plan use budget-forecast; to choose cash versus a financing arrangement use financing-strategy."
license: MIT
---

# Cash Flow Forecast

Show when strategic plans create liquidity pressure and which assumptions drive it.

## Establish the Decision Frame

- Read `.agents/ecom-finance.md` if it exists, then state the entity/consolidation scope, monthly forecast horizon, opening as-of date, currency, accounting basis and close status, and the funding or operating decision.
- Define available cash: bank-reconciled cash available for operations. Show restricted cash, undrawn facilities, reserves, and trapped/entity-specific cash separately.
- Record the user-supplied minimum cash floor and materiality. If either is absent, show the full result and every variance without inventing a threshold or claiming a breach.
- Route weekly or 13-week liquidity work to `thirteen-week-cash-flow`, the integrated operating plan to `budget-forecast`, detailed PO/unit timing to `demand-planning`, and cash-versus-financing selection to `financing-strategy`.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/entity coverage`, `control total`, `tie-out status`, and `limitations`. Register bank reconciliations, channel and processor payout schedules, AR/AP, sales forecast, PO/deposit/freight schedules, payroll, operating commitments, debt, taxes, distributions, capex, and approved facilities.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Keep actual cash, base forecast, downside, and growth scenarios in separate columns or tables. If opening available cash cannot be tied to reconciled evidence, or material receipt/disbursement schedules are unavailable, return `Insufficient evidence` with the partial forecast, blocked conclusions, and required sources.

## Forecast Logic

Use a direct cash convention: inflows and outflows are entered as positive amounts, and

`ending available cash = beginning available cash + cash receipts - cash disbursements + financing inflows - financing repayments +/- cash transfers to or from entities outside the forecast scope`.

Show formulas and normalize signed source data to this convention. Ending cash for one period must equal the next period's beginning cash. Eliminate transfers among bank accounts or entities inside the consolidated forecast scope; if transfers cross the defined scope, show the external side once and name the counterparty scope.

- Model channel receipts on expected settlement dates, net or gross exactly as the source provides; do not double-count fees withheld from payouts.
- Separate sales-tax collections/remittances and other pass-through amounts from revenue.
- Place inventory deposits, final payments, freight, duties, and supplier terms on expected cash dates, not accounting-expense dates.
- Separate debt principal, interest, facility draws, distributions, and capex. Show restricted cash and facility availability outside operating cash.
- Build base, downside, and growth scenarios from explicit driver changes such as settlement lag, conversion/ad cost, inventory deposit, supplier timing, or large payments. Never convert a missing input into a downside assumption without labeling it.

## Deliverable

Return the decision frame and source register, monthly cash table by scenario, opening-cash reconciliation, lowest cash point/date, headroom to the user-supplied floor, runway definition and result, material sensitivities, unresolved evidence, and draft management options with timing and decision owner.

## Quality Gate

- Each opening balance ties to registered evidence and each rollforward foots; unexplained differences remain visible.
- Inter-account and within-scope intercompany transfers eliminate; out-of-scope transfers appear once.
- Receipt/disbursement detail ties to disclosed control totals or includes reconciling items.
- Actual, forecast, and scenario values are visually and semantically distinct.
- No scenario changes only revenue while ignoring its inventory, fulfillment, fee, tax, or working-capital effects.
- Do not call a credit limit cash or claim runway beyond the evidenced horizon.

## Guardrails

Stage the forecast and management options as drafts only. Never initiate transfers, draw debt, change payment dates, place purchase orders, send the forecast, or change banking/system access. Financing, covenant, tax-payment, and distribution decisions require review and authorization by the responsible qualified parties.
