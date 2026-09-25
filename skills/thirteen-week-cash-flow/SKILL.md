---
name: thirteen-week-cash-flow
description: "Build direct-method 13-week cash forecasts for weekly ecommerce liquidity across cash, receipts, AP, inventory, payroll, and debt. Use cash-flow-forecast for monthly planning and financing-strategy for funding."
license: MIT
---

# 13-Week Cash Flow

Estimate when available cash may breach a user-approved reserve and identify actions early enough to matter.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity/account scope, bank cutoff timestamp, 13 weekly ending dates, as-of date, currency and FX policy, cash basis for the forecast, accounting close status, approved minimum reserve, decision owner, and decisions required.

Use this skill for tactical weekly receipts and disbursements. Route strategic monthly, growth, or multi-year scenarios to `cash-flow-forecast`; cash-versus-financing or facility selection to `financing-strategy`; structural inventory/AR/AP terms to `working-capital`; and SKU purchasing logic to `demand-planning`.

## Evidence Gate

Create a source register with `line/input`, `source`, `extract date`, `covered period`, `entity/account grain`, `coverage`, and limitation. Include bank reconciliations, processor payout schedules, AR, AP, payroll dates, approved POs, supplier/freight commitments, cards, ads, debt agreements, tax payments, owner activity, and one-time items. Label every value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate actual weeks, the frozen prior forecast, the current forecast, and scenarios. Reconcile opening available cash to banks at the cutoff. Show restricted cash separately and undrawn credit as availability, not cash. Eliminate inter-account and intercompany transfers from consolidated cash flow or show both sides so they net to zero.

Map each economic receipt once. Channel sales are not cash receipts: use the processor/marketplace deposit date and choose either net settlement or gross settlement with fees/refunds shown separately. Never count both channel sales and the related processor deposit.

Use user-defined materiality for variance commentary. Without it, report all actual-versus-prior-forecast variances and let the user choose a review filter. If opening cash cannot be reconciled or material receipt/payment timing is unavailable, issue a provisional schedule with affected rows marked unavailable and a data request; do not report a precise lowest-cash amount.

## Direct-Method Model

Display inflows and outflows as positive amounts in their sections and calculate:

`ending available cash[t] = beginning available cash[t] + operating receipts[t] - operating disbursements[t] + financing inflows[t] - financing outflows[t]`

`beginning available cash[t+1] = ending available cash[t]`

`headroom[t] = ending available cash[t] - approved minimum reserve[t]`

`variance[t,line] = actual[t,line] - frozen prior forecast[t,line]`

Receipts include dated processor/marketplace settlements, wholesale/retail collections, other AR, and verified other cash inflows. Disbursements include inventory deposits/finals, freight/duties, fulfillment, payroll, ads, refunds, cards, software, rent, contractors, professional fees, taxes, capex, and other payments. Financing shows debt draws, principal, interest/fees, owner contributions, and distributions separately.

For each forecast amount state the timing driver and evidence. Build a downside scenario for decision-critical settlement, sales, inventory, or payment timing, but keep it outside the current forecast. Do not net unrelated receipts and disbursements merely to make the schedule shorter.

## Weekly Control Cycle

At each roll-forward:

1. Freeze and retain the prior version.
2. Replace completed weeks with bank-reconciled actuals.
3. Explain actual-versus-prior-forecast and forecast-versus-prior-forecast changes.
4. Append a new week so the horizon remains 13 weeks.
5. Recalculate the lowest-cash week, reserve headroom, scenario breaches, and action deadlines.

## Deliverable

Return:

1. A spreadsheet-ready 13-week direct-method table with actual/prior/current/scenario clearly separated.
2. Opening-cash reconciliation, source register, assumptions, coverage, and unavailable-item schedule.
3. Variance report with cause, timing/permanent classification, owner, and forecast treatment.
4. Lowest projected cash and reserve headroom, qualified by evidence status.
5. An action register with amount, action type, owner, approval, deadline, latest safe decision date, dependency, and downside if missed.

## Quality Gate

- Each week cross-foots, and every next-week beginning balance equals the prior ending balance.
- Opening and actual cash tie to reconciled bank control totals, with transfers eliminated.
- Every material forecast row traces to a dated source or visible assumption.
- Processor/channel receipts, cards, debt, and owner activity are neither double counted nor incorrectly netted.
- Actual, prior forecast, current forecast, and scenario remain separate, and no unavailable value is zero.

## Guardrails

Stage forecasts and action options only. Never initiate or delay a payment, draw debt, contact a bank/vendor/customer, change access, submit lender reporting, post/send, or move cash without approval. Do not claim financing, collection, payment deferral, or covenant capacity without evidence. Obtain qualified treasury/accounting review for material liquidity decisions, lender review for agreement reporting, and legal/tax review where required.
