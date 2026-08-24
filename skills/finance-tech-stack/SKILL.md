---
name: finance-tech-stack
description: "Audit or design ecommerce finance-system architecture across accounting, channel connectors, inventory, payroll, spend, forecasting, reporting, and integrations. Use for requirements, tool selection, system-of-record design, or migration planning. For book reliability use accounting-quality-audit; for control design use internal-controls."
license: MIT
---

# Finance Tech Stack

Choose an evidence-backed architecture that the actual team can operate, reconcile, and exit.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity/consolidation scope, assessment as-of date, currency, accounting basis and latest close status, target decision, timeline, budget/TCO horizon, owner capacity, and non-negotiable requirements. Capture channels, order volume, SKU count, locations, jurisdictions, transaction complexity, and current pain without assuming that scale alone requires a larger platform. Use the user's materiality or risk threshold for gaps; if none is supplied, report every identified gap without silently choosing one.

Route book-reliability questions to `accounting-quality-audit`, approval/access-control design to `internal-controls`, and dashboard metric design to `kpi-dashboard`. Do not activate this skill merely because a user mentions a product while asking how to perform an unrelated task in it.

## Evidence Gate

Create a source register with `source`, `publication/extract or as-of date`, `entity/process coverage`, `control total or verification performed`, and `limitations`. Register the current architecture, contracts/invoices, process maps, close issues, reconciliation evidence, data volumes, team interviews, and vendor claims.

Verify current vendor capabilities, pricing, limits, security claims, integrations, and support against dated official sources. If live verification is unavailable, label the claim `unavailable` or `assumption`; do not recommend from memory as current fact. Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Separate current actual cost/performance, forecast-state estimates, and scenarios.

If requirements, current data flows, or ownership are too incomplete to compare options, return `Insufficient evidence`, a provisional requirements map, and the exact discovery needed before selection.

## Architecture and Evaluation

Map each finance object to one accountable system of record, upstream sources, transformations, downstream reports, reconciliation/control total, owner, failure alert, and recovery path. Cover accounting, channel connectors, inventory/landed cost, payroll, AP/spend, banking/cards, forecasting/reporting, warehouse/BI, and close workflow only where relevant.

Build requirements before naming products. Use user-approved weights and show the scoring formula; if weights are absent, present an unweighted comparison rather than inventing priorities. Evaluate data accuracy, integration quality, reconciliation, close speed, reporting utility, access/audit logs, security evidence, export/API limits, portability, scale, support, implementation capacity, and reversibility.

Show `TCO = implementation + migration + recurring fees + integration/maintenance + valued internal effort`, with period, currency, inputs, and assumptions. Do not claim savings or ROI without an evidenced baseline. Identify personal/sensitive data paths, retention, least privilege, MFA/SSO needs, and vendor-exit/export controls without asserting compliance from a logo or marketing page.

## Deliverable

Return the decision frame and source register, current system/data-flow map, requirements and gap register, option matrix with evidence and scores, recommended architecture with alternatives, TCO scenarios, control/reconciliation design, and phased migration plan with owners, dependencies, cutover acceptance tests, rollback, and risks.

## Quality Gate

- Every vendor claim is dated and traceable to an official source; unknowns remain visible.
- Each material data object has a system of record, owner, control total, and failure/recovery path.
- Current actuals, proposed-state forecast, and scenarios are separate; formulas and score/TCO sign conventions are shown.
- No recommendation depends on an invented benchmark, hidden weight, missing-as-zero input, or untested migration assumption.

## Guardrails

Stage architecture, vendor comparisons, and migration plans as drafts only. Never purchase/sign, install, connect accounts, migrate/delete data, send vendor messages, move cash, or change access. Security, privacy, accounting, legal, procurement, and contractual claims require review by their responsible qualified owners.
