---
name: accounting-quality-audit
description: "Audit ecommerce book reliability for forecasts, margin, cash, lending, board, or KPI decisions; diagnose untrusted financials. Use internal-controls for controls and inventory-cogs for inventory tie-outs."
license: MIT
---

# Accounting Quality Audit

Determine which decisions the books can support, with traceable evidence and purpose-specific readiness.

## Establish the Decision Frame

- Read `.agents/ecom-finance.md` if it exists, but verify facts against current evidence.
- State the entity or consolidation scope, reporting period and as-of date, functional/presentation currency, accounting basis, close status, and the decision the books must support.
- Record the user's materiality threshold. If none is supplied, report every detected variance and rank by magnitude; do not silently choose what is immaterial.
- Assess each intended use separately. Books can be adequate for liquidity monitoring yet inadequate for SKU margin or lender reporting.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period and entity coverage`, `control total`, `tie-out status`, and `limitations`. Prefer the trial balance/general ledger, statements, bank and card reconciliations, channel order reports, processor/marketplace settlements, inventory subledger, debt schedules, payroll/AP support, and close checklist.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`. Missing is never zero. Keep actual, forecast, and scenario data separate; forecasts are not evidence that actual balances are correct. If the minimum evidence for the named decision is unavailable, stop at an `Insufficient evidence` result that lists the missing evidence and the conclusions that cannot be made.

## Audit Tests

- Test completeness, existence, accuracy/valuation, cutoff, classification, and rights/obligations where relevant.
- Bridge channel gross orders through discounts, refunds, chargebacks, gift-card/deferred-revenue activity, settlements, receivables/clearing accounts, and recorded revenue. Show the formula and sign convention.
- Tie balance-sheet accounts to independent reconciliations and inspect stale clearing items, unusual signs, unsupported journals, and post-extract changes.
- Test inventory and COGS timing, landed-cost policy, returns, shrinkage, and subledger-to-GL differences; route a detailed tie-out to `inventory-cogs`.
- Review expense classification, accruals, prepaids, deferred revenue, debt, payroll, owner activity, and close/reviewer evidence.
- Confirm control equations such as `assets = liabilities + equity` and `beginning cash + net cash movement = ending cash`; explain every residual rather than forcing a tie.

## Deliverable

Return:

1. `Scope and evidence`: decision frame, source register, coverage, and unresolved conflicts.
2. `Readiness by use case`: green, yellow, red, or insufficient evidence, with explicit criteria and evidence for each rating.
3. `Findings`: account/process, assertion, reported and recalculated amounts, formula/sign convention, variance, cause or labeled hypothesis, decision impact, and confidence.
4. `Fix queue`: immediate, next close, and later, with owner, evidence required, and completion test.
5. `Owner explanation`: what the books can and cannot currently support in plain language.

## Quality Gate

- Every conclusion must trace to a registered source and period; every calculated figure must show inputs and formula.
- Totals must tie to disclosed control totals or show a reconciling-items table. Never plug an unexplained variance.
- Do not issue one overall readiness color when use cases differ, and do not treat a clean P&L as proof of a clean balance sheet.
- Recheck whether the ledger or source report changed after extraction before calling the assessment current.

## Guardrails

Stage findings and proposed corrections as drafts only. Never post journal entries, alter source records, send a report, move cash, or change access. Do not present this management diagnostic as an independent financial-statement audit, review, compilation, attestation, or assurance engagement. Accounting-policy conclusions and correcting entries require review by the responsible controller or qualified accountant.
