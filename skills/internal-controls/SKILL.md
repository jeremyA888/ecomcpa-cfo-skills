---
name: internal-controls
description: "Assess or design ecommerce finance controls for approvals, reconciliations, access, fraud/error prevention, segregation of duties, close review, or audit-readiness preparation. Use for process-risk and control-matrix work. For whether historical books are decision-ready use accounting-quality-audit; for finance-system architecture use finance-tech-stack."
license: MIT
---

# Internal Controls

Identify evidence-backed control gaps and proportionate, operable responses without implying audit assurance.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity/process scope, assessment period and as-of date, currency, accounting basis and latest close status, control objective, intended reliance, decision, systems, roles, and team-capacity constraints. Record user-defined materiality/risk criteria; if absent, report all identified exceptions without inventing a severity cutoff.

Route reliability of historical balances to `accounting-quality-audit`, technology architecture to `finance-tech-stack`, and a specific inventory reconciliation to `inventory-cogs`. This skill may assess design or observed operation; it does not perform an audit or attest to effectiveness.

## Evidence Gate

Create a source register with `source`, `extract/interview/as-of date`, `period/process/entity coverage`, `population and sample/control total`, `verification performed`, and `limitations`. Register policies, role/access exports, workflow configurations, approval/reconciliation evidence, change logs, exception reports, close artifacts, and interviews.

Label every key fact or score `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero or “no exception.” Keep actual/current controls, forecast or proposed future controls, and stress/fraud scenarios separate. Test operating effectiveness only when dated execution evidence and a disclosed population/sample exist; otherwise assess design only. If evidence is inadequate, return `Insufficient evidence`, a design-only view, and the tests needed for operating conclusions.

## Control Assessment

Cover only relevant areas: bank/card/processor access, vendor master and payments, POs/receipts/inventory custody, payroll/owner pay, refunds/discounts/gift cards/chargebacks, journals and balance-sheet reconciliations, system administration/integrations, close review, and sensitive-data access.

For each risk, document the control objective or financial assertion, inherent-risk rationale, existing control, owner, cadence, preventive/detective nature, evidence retained, segregation-of-duties conflicts, design status, operating-test result, exception, and residual-risk rationale. For lean teams, identify a specific compensating review rather than demanding impossible segregation.

Show formulas and sign conventions for any score or exception rate, such as `exception rate = exceptions / items tested`; never invent weights, benchmarks, or likelihood values. Sample counts must tie to the registered population or disclose coverage limits.

## Deliverable

Return the decision frame and source register, risk-control matrix, role/access and segregation map, exception log, design-versus-operation conclusion, prioritized remediation plan with owner/date/completion evidence, and a proportionate future testing plan. Keep reported control failures distinct from hypothetical fraud scenarios.

## Quality Gate

- Every operating-effectiveness conclusion cites execution evidence, period, population, sample, and exception result.
- Proposed controls are feasible for the named roles/systems and have an owner, cadence, evidence artifact, and fallback/compensating control.
- Actual state, future design, and scenarios are separate; unavailable evidence remains visible.
- Residual-risk/severity language follows user-approved criteria or is presented qualitatively with no invented threshold.

## Guardrails

Stage assessments, control matrices, and remediation plans as drafts only. Never approve transactions, change roles/access/configuration, contact vendors or staff, send reports, post entries, or move cash. Do not claim independent assurance, compliance, fraud absence, or control effectiveness beyond tested evidence; describe audit readiness as a management preparation assessment. Material accounting, security, legal, HR, and assurance conclusions require review by the responsible qualified professionals.
