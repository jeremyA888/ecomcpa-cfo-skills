---
name: ecom-finance-context
description: "Create, update, or read a reusable, non-sensitive ecommerce CFO context file for an authorized brand workspace. Use to preserve finance definitions, systems, constraints, evidence status, and open questions for other CFO skills. Do not use it to store raw financials, transactions, credentials, account identifiers, or personal data."
license: MIT
---

# Ecommerce CFO Context

Create or update `.agents/ecom-finance.md` only when persistent workspace context is authorized. Other CFO skills may read it as a lead, but current source evidence always outranks it.

If the user asks only to read, explain, or summarize existing context, do not modify the file; return its dated scope, limitations, and stale or conflicting fields.

## Establish the Decision Frame

State the legal entity/consolidation scope, context as-of date, presentation/functional currency, timezone and fiscal calendar, accounting basis and latest close status, intended users, and decisions this context may support. Record the user's materiality definition; if none exists, write `unavailable` rather than inventing one.

Before writing, determine whether the destination is tracked and whether the repository is public, private, or unknown. State the exact path and visibility result. The user's explicit request to create/update this file authorizes that file edit, but not inclusion of sensitive content; if visibility or content authorization is unclear, return a staged preview instead of persisting it.

## Evidence Gate

Use only user-provided or clearly in-scope workspace sources. Check existing `.agents/ecom-finance.md`, then `.claude/ecom-finance.md` only as a migration lead; do not broadly harvest finance documents. Create a source register with `source ID`, `source/report`, `extract or as-of date`, `entity/period coverage`, `control total or verification performed`, and `limitations`.

Label every substantive value `reported`, `calculated`, `assumption`, or `unavailable`, followed by its source ID and verified/as-of date. Missing is never zero. Keep historical actuals, current forecast, targets, and scenarios in distinct fields. When sources conflict, preserve both values and mark the conflict; never resolve it silently.

## Context Schema

```markdown
# Ecommerce CFO Context

## Document Control
- Entity/scope; as-of date; currency; timezone/fiscal calendar
- Accounting basis; latest close period/status; context owner/reviewer
- Repository visibility and approved persistence scope
- Allowed uses; materiality definition; last updated

## Value Labels
- reported | calculated | assumption | unavailable

## Source Register
| ID | Source/report | Extract/as-of | Coverage | Verification/control total | Limitations |

## Business and Operations
- Brand/business model, channels/markets, products/SKUs, fulfillment/locations
- Supplier/manufacturing model, order-to-cash, returns/refunds, settlement timing

## Systems and Ownership
- System of record by finance object, integrations, process owner, close cadence
- Store system names and roles only; never credentials or account identifiers

## Accounting and Metric Policies
- Revenue/returns/gift cards, inventory valuation and landed cost, close/cutoff
- Gross sales, net revenue, gross margin, contribution margin, CAC/LTV and other KPI formulas
- Formula, sign convention, units, source, and approved owner for each metric

## Current Actual Snapshot
- Latest closed period and reconciled control totals only; link source IDs

## Forecasts, Scenarios, and Decision Thresholds
- Baseline forecast, named scenarios, cash floor, targets, covenants, planning constraints
- Keep forecasts/scenarios separate from actuals and name the approving owner/date

## Data Quality and Open Decisions
- Known gaps/conflicts, affected decisions, evidence needed, owner, next review date

## Change Log
- Date, field, prior value/status, new value/status, source, reason, editor
```

## Deliverable

Return the proposed or updated context, source register, unresolved conflicts, excluded sensitive items, and a change summary. If evidence is insufficient, add an `Insufficient evidence` section, preserve the schema with `unavailable` fields, and list the minimum follow-up; do not fill gaps from general knowledge.

Route analysis itself to the relevant specialist: `accounting-quality-audit`, `budget-forecast`, `cash-flow-forecast`, `channel-profitability`, `demand-planning`, `finance-tech-stack`, `financial-reporting`, `internal-controls`, `inventory-cogs`, or another installed CFO skill. This skill records approved context; it does not make the underlying decision.

## Quality Gate

- Every substantive field has a value label, source ID, and as-of/verified date; calculations show formulas and sign conventions.
- Context control totals tie to registered evidence or remain visibly unresolved.
- Actuals, forecasts, targets, and scenarios are never blended.
- A newer assumption never overwrites an older reported fact; stale facts remain dated rather than presented as current.
- The file contains no secrets, raw transaction detail, personal data, bank/card/account numbers, tax IDs, tokens, credentials, or sensitive access details.

## Guardrails

Stage a preview when persistence or sensitivity is unresolved. Write only the authorized context path; never commit, publish, send, or sync it without separate authorization. Never post entries, move cash, change system access, or copy sensitive finance data into the context. Refer accounting-policy, legal, tax, covenant, and regulated conclusions to the responsible qualified reviewer.
