---
name: financial-reporting
description: "Create evidence-backed ecommerce management reporting packs and period commentary from supplied financials. Use for monthly results, executive finance summaries, and internal or board reporting. For dashboard specifications use kpi-dashboard; for financing/covenant packages use lender-investor-package; for unreliable books use accounting-quality-audit."
license: MIT
---

# Financial Reporting

Explain closed or explicitly preliminary results without inventing numbers or causes.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity/consolidation scope, reporting period and as-of date, currency, accounting basis, close status, audience, comparator periods/plan, and decisions required. Mark the pack `preliminary`, `final`, or `insufficient evidence` prominently.

Record the user's materiality threshold for commentary. If none is supplied, disclose all detected variances and rank by magnitude; do not silently suppress or call a variance immaterial. Route metric/dashboard specification to `kpi-dashboard`, financing/covenant submission to `lender-investor-package`, and source-book reliability concerns to `accounting-quality-audit` before presenting conclusions as final.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/entity coverage`, `control total`, `tie-out status`, and `limitations`. Register the trial balance/ledger and statements, reconciliations, channel sales, inventory, cash/debt, approved forecast/budget, KPI sources, and any prior comparison pack.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Keep actual, forecast, target, and each scenario in separate columns or sections. If statements do not tie, close status is unknown, or evidence cannot support material sections, return the valid partial pack plus `Insufficient evidence`, blocked commentary, and a specific request list.

## Report Pack

- Scope, close status, evidence coverage, and source register.
- Executive summary separating observed result, evidenced driver, implication, and draft decision.
- P&L, balance sheet, and cash/working-capital view to the extent supported; do not imply a complete statement set when one is absent.
- Revenue by channel/product, company-defined gross and contribution margin, operating expenses, inventory health, debt/obligations, and KPIs relevant to the decision.
- KPI and variance tables with current actual, prior/comparator, forecast/target, variance, formula, units, and source.
- Wins, risks, decisions, owners, and next actions.

Use `variance = actual - comparator` and `variance % = variance / abs(comparator)` when the denominator is nonzero. State the sign convention and label favorable/unfavorable based on line type. Explain what happened, why, why it matters, and what to do next; a causal statement without evidence must be labeled `assumption`, not written as fact.

## Deliverable

Return the report pack or a clearly labeled outline when evidence is incomplete, including the decision frame, sources, calculation definitions, control-total reconciliation, commentary, and unresolved evidence. Use plain language while preserving accounting meaning.

## Quality Gate

- Statements and detail tie to disclosed control totals or show visible reconciling items; rounding differences are identified.
- Metric definitions match the approved context and landed cost is not counted twice across gross and contribution margin.
- Actual, forecast, target, and scenarios are distinct; all numbers carry status and source lineage.
- Each causal claim has evidence; hypotheses and forward-looking implications remain labeled.
- Preliminary or incomplete books cannot produce a visually or verbally “final” pack.

## Guardrails

Stage packs, commentary, and decisions as drafts only. Never post entries, send/share/publish a pack, move cash, change access, or alter source reports. Protect confidential financial data. Accounting-policy, covenant, tax, legal, board, and external-use conclusions require review and approval by the responsible qualified parties.
