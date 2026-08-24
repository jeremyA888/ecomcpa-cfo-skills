---
name: financing-strategy
description: "Choose cash, partial financing, lines, supplier/PO/inventory/receivables finance, or a funding mix for ecommerce orders. Use cash-flow skills for forecasts and lender-investor-package for submission materials."
license: MIT
---

# Financing Strategy

Choose the funding arrangement that preserves resilience and creates the best risk-adjusted economics, not merely the lowest advertised rate.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record the legal entity and guarantor scope, decision and owner, as-of date, currency and FX policy, accounting basis and close status, amount, purpose, cash dates, decision deadline, user-approved minimum cash reserve, materiality, forecast horizon, and risk constraints.

Choose the applicable mode:

- **Transaction funding:** cash versus partial or full financing for a specific PO, inventory build, launch, or contracted order.
- **Capital structure:** compare facilities or capital sources for recurring working capital, growth, refinancing, or a defined investment.

Use `demand-planning` for order quantity and timing, `thirteen-week-cash-flow` for weekly liquidity, `cash-flow-forecast` for strategic runway, `working-capital` for structural inventory/AR/AP levers, and `lender-investor-package` after an instrument is selected and evidence must be packaged.

## Evidence Gate

Create a source register with `input`, `source/counterparty`, `extract or as-of date`, `covered period`, `entity/grain`, `control total`, `verification status`, and limitation. Include reconciled available cash, restricted cash, approved reserve policy, base and downside cash forecasts, order and supplier schedules, expected customer receipts, unit/contribution economics, debt schedule, signed facilities, current term sheets, borrowing-base inputs, covenants, liens, guarantees, owner distributions, taxes, and other committed uses of cash.

For every option, build a term register covering committed and usable amount, eligibility, advance rate and reserves, draw/repayment timing, interest basis, every fee, maturity/amortization, prepayment or sales-remittance sweep, collateral/lien priority, recourse and guarantees, covenants, reporting/field-audit burden, events of default and cure, default pricing, cross-defaults, cash dominion/lockbox rights, discretionary or material-adverse-change funding stops, intercreditor/subordination terms, renewal/cancellation rights, funding certainty, and legal/entity restrictions. Verify current product claims and terms from official documents or the counterparty; remembered rates or marketing summaries are not decision evidence.

Label key values `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Keep actuals, the approved forecast, and each financing scenario separate. Use the user's materiality and reserve policy. If the reserve, cash forecast, transaction economics, or executable terms are missing, return a provisional option screen and data request rather than naming a winner.

Use aggregated schedules and governed source pointers wherever possible. Do not persist or reproduce bank/account numbers, tax identifiers, personal financial statements, identity documents, credentials, customer-level data, or unredacted guarantee/application materials in the analysis.

## Build Comparable Funding Cases

Define unrestricted, bank-reconciled cash available for operations. Show restricted or trapped cash and undrawn facilities separately; a credit limit is not cash. Put every transaction cash flow on its expected date, including supplier deposits/finals, freight, duty, tax, inspection, insurance, refunds, fulfillment, fees, and customer settlement timing.

For each option and period, calculate:

`net usable financing proceeds = gross draw - upfront fees - lender holdbacks/reserves - other amounts withheld at funding`

`ending available cash = base ending cash before the transaction - incremental transaction outflows + incremental transaction receipts + net usable financing proceeds - principal repayments - later-paid financing interest and fees`

`reserve headroom = ending available cash - approved minimum reserve`

`funding gap = max(0, approved minimum reserve - ending available cash before new financing)`

The minimum financing need is the gross draw that produces enough dated net usable proceeds to cover the greatest funding gap under the proposed mechanics. If a variable upfront fee is withheld, solve `gross draw = (funding gap + fixed upfront costs) / (1 - variable upfront fee rate)`. Round the gross draw upward to the smallest currency unit so rounded proceeds still cover the funding gap, unless verified counterparty fee-rounding mechanics support a different result; then recompute the fee and net usable proceeds from the rounded draw. Apply commitment, borrowing-base, advance-rate, reserve, and draw-condition limits from signed terms. Add a buffer only when management supplies or approves it; do not disguise an invented cushion as policy.

Calculate transaction economics without treating borrowing as revenue:

`cash contribution before financing = transaction cash receipts - refunds and pass-through taxes - product/landed cost - fulfillment/shipping/fees/marketing - other incremental cash costs`

`cash contribution after financing = cash contribution before financing - financing interest and fees`

Calculate interest from the expected daily or disclosed periodic balance and day-count convention. Total cash financing cost includes interest, origination, commitment/unused, monitoring, audit/appraisal, legal/filing, wire, factoring discount, prepayment, and other required fees. Keep principal repayment, financing cost, and any accounting expense classification distinct.

For a single draw and repayment, calculate `periodic cost rate = total financing cost / net usable proceeds` and `effective annualized rate = (1 + periodic cost rate)^(365 / days outstanding) - 1`. For multiple dated cash flows, use a disclosed dated-cash-flow IRR convention with borrower receipts positive and borrower payments negative. If dates or net proceeds are unavailable, do not report an effective rate. Show dollar cost alongside the rate and do not rank short-term options on APR alone. Present after-tax cost only when the applicable tax treatment and ability to realize the benefit are supported.

Define the zero-contribution financing break-even as `transaction cash receipts = non-financing transaction cash outflows + financing interest and fees`. If management requires a minimum contribution or return, add that approved amount separately. Do not invent an opportunity-cost break-even for balance-sheet cash without a specific competing use.

Screen cash, supplier terms, customer deposits where lawful and operationally supportable, cards or charge facilities, revolvers, transaction/PO finance, inventory or receivables facilities, factoring, sales-remittance or revenue-based products, term debt, and owner/equity capital only when relevant. Do not translate dilution, control rights, liquidation preferences, personal guarantees, or collateral loss into a fake interest rate; present those risks separately. Count cash opportunity cost only when a specific competing use and its evidence-backed outcome are modeled.

For capital-structure mode, size facilities to the dated base and required downside funding curve, not revenue or inventory alone. Match self-liquidating working assets to revolving or transaction facilities and longer-lived uses to compatible tenor; do not fund a permanent structural cash deficit with debt that depends on repeated short-term renewal.

After the same feasibility gates used for transaction funding, compare surviving structures on total cash cost under the same utilization, liquidity/headroom, downside debt service and repayment source, tenor and renewal risk, collateral/liens/guarantees, covenant headroom, reporting burden, execution certainty, flexibility, and ownership/control effects. Use management's stated priorities or weights. If none are supplied and no option dominates, present the efficient tradeoffs and decision needed rather than inventing a single best arrangement.

## CFO Decision Rule

Eliminate an option if it breaches the approved reserve in base or required downside cases, cannot fund on the required dates, lacks evidenced availability, mismatches asset conversion and repayment timing, makes the transaction uneconomic, creates an unmanageable covenant/collateral/guarantee exposure, or cannot be repaid from an identified source.

For transaction funding, recommend the smallest funding mix that preserves approved headroom and downside resilience at the best supported total tradeoff. Compare all-cash, minimum partial financing, a management-approved buffered draw, and full financing when available. For capital structure, name a winner only when it survives every feasibility gate and either dominates the alternatives or management's stated priorities resolve the tradeoff. Cash is not automatically free, and debt is not automatically prudent because expected contribution exceeds interest. State decision triggers that would change the recommendation, including order delay, demand/returns, settlement lag, borrowing-base erosion, covenant headroom, FX, or a competing cash use.

## Deliverable

Return the decision frame and source/term registers, dated transaction or capital-need cash schedule, option scorecard, cash-versus-partial-versus-full or capital-structure scenarios, reserve headroom and downside low point, all-in financing cost and break-even, contribution after financing where applicable, covenant/collateral/guarantee and ownership/control implications, recommended funding mix with rationale and confidence, decision triggers, open evidence, and a staged decision/action register. If evidence is insufficient, rank only the supported dimensions and name the blocked conclusion.

## Quality Gate

- Reconcile opening cash, base forecast, order schedule, debt, and option terms to registered controls.
- Reperform dated cash, reserve, interest, fee, break-even, and contribution calculations; no draw or principal repayment is profit or operating expense.
- Confirm a grossed-up draw follows verified fee rounding, rounds upward by default, and still delivers at least the required net proceeds.
- Confirm restricted cash, facility availability, processor receipts, supplier payments, and transaction costs appear once.
- Confirm the selected option remains feasible under required downside timing and does not rely on an invented probability, renewal, waiver, or borrowing base.
- Calculate covenant headroom only from signed definitions; do not substitute generic DSCR, fixed-charge, leverage, or borrowing-base formulas.
- Confirm current term evidence, confidentiality, and qualified accounting, tax, legal, and lender review needs are visible.

## Guardrails

This skill is advisory-only. Never apply for financing, contact a capital provider or supplier, accept or sign terms, pledge assets, guarantee debt, draw a facility, issue equity, place/cancel an order, change payment timing, send materials, or move cash; user approval does not expand this skill into execution. Do not promise funding, lender eligibility, covenant compliance, legal enforceability, tax treatment, customer demand, or investment returns. Material financing decisions and any separately authorized execution require the responsible decision makers and appropriate treasury, accounting, tax, legal, and lender review.
