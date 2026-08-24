---
name: working-capital
description: "Analyze ecommerce working capital, cash conversion, inventory, receivables, payables and supplier terms. Use financing-strategy for funding, thirteen-week-cash-flow for timing, and demand-planning for SKU buys."
license: MIT
---

# Working Capital

Quantify where operating cash is tied up and distinguish liquidity timing from profit.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity and account scope, measurement period and as-of date, currency and FX policy, accounting basis, close status, working-capital definition, decision, decision owner, and operational constraints.

Route weekly receipt/payment timing to `thirteen-week-cash-flow`, SKU reorder logic to `demand-planning`, inventory reconciliation to `inventory-cogs`, cash-versus-debt or facility selection to `financing-strategy`, and debt application/covenant materials to `lender-investor-package`.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `entity/account/SKU grain`, `coverage`, and limitation. Include closed balance sheet and P&L, inventory subledger, AR/AP aging, credit purchases or an identified proxy, supplier terms, processor settlements/reserves, open POs, debt agreements, and cash forecast. Label each value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate actual, forecast, and scenario. Tie inventory, trade AR, processor receivables, trade AP, short-term debt, and other included balances to closed controls. Reconcile operational detail to those balances and identify late postings, in-transit inventory, disputed balances, affiliate items, and non-operating accounts.

Use user-defined materiality. Without it, show all reconciliation and period variances. If average balances, credit sales/purchases, aging, or agreement terms are unavailable, label the affected metric unavailable or identify a proxy explicitly; do not silently substitute ending balances or COGS.

## Metric and Cash-Release Model

State the day count and any annualization. Use consistent positive balance conventions:

- `average balance = (beginning balance + ending balance) / 2`, or a disclosed higher-frequency average.
- `inventory turns = period recognized COGS / average inventory`; annualize only with a stated factor.
- `DIO = average inventory / period recognized COGS x days in period`.
- `DSO = average trade AR / net credit sales x days in period`; do not include immediate card sales as credit sales.
- `DPO = average trade AP / credit purchases x days in period`; if COGS is used as a proxy, label and quantify the limitation.
- `CCC = DIO + DSO - DPO` under the recorded balance classifications.
- `net operating working capital = included operating current assets - included operating current liabilities`; list whether cash, debt, taxes, and other items are excluded.
- `cash released from an operating-asset reduction = actual baseline asset - scenario asset`.
- `cash released from an operating-liability increase = scenario liability - actual baseline liability`; both release formulas describe timing/liquidity, not profit.

If a ratio denominator is zero or negative, report the result as `not meaningful` and explain the driver rather than forcing a rate.

Show processor/marketplace settlement receivables and weighted settlement lag separately. Add settlement lag to an operating cash-cycle bridge only if it is not already captured in DSO; never count it twice.

Model inventory/PO timing, supplier deposits and terms, collections, processor timing, and AP scheduling as separate levers. Quantify baseline, scenario, cash release/use, profit or fee effect, implementation cost, timing, operational constraint, covenant effect, and downside. Never assume a supplier, processor, or lender will accept changed terms.

## Deliverable

Return:

1. A reconciled working-capital baseline with formulas, balances, days/turns, trends, source coverage, and value labels.
2. A bridge separating inventory, trade AR, processor settlement, trade AP, other operating balances, and financing.
3. Scenario table with cash release/use, profit effect, timing, cost, risk, dependency, confidence, and no double counting.
4. Action register with owner, counterparty approval needed, evidence, deadline, operational guardrail, and rollback/review point.
5. Source register, reconciliation report, proxy/unavailable list, and next-data plan.

## Quality Gate

- Tie all included balances and period flows to closed control totals.
- Reperform average-balance, turns, days, CCC, and cash-release formulas using the stated day count.
- Confirm processor lag, trade AR, inventory in transit, AP, deposits, and financing are classified once.
- Confirm working-capital cash release is not labeled profit and financing availability matches signed evidence.
- Confirm actual, forecast, and scenario remain separate and no unavailable input appears as zero.

## Guardrails

Stage analysis and negotiation options only. Never reschedule AP, change supplier/processor terms, place or cancel POs, draw/refinance debt, contact counterparties, change access, post/send, or move cash without approval. Do not recommend breaching terms, covenants, controls, or supplier/customer obligations. Obtain qualified accounting/tax review for classification, lender review for financing/covenants, and legal or procurement review for contractual changes where required.
