---
name: staffing-plan
description: "Build ecommerce headcount, payroll, contractor, owner-compensation, capacity, and hire-affordability scenarios. Use for workforce budgets or hire timing. Use profit-improvement for broad cost reduction and thirteen-week-cash-flow for weekly liquidity effects."
license: MIT
---

# Staffing Plan

Connect workforce decisions to capacity, service, profit, and dated cash while protecting personal data.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists. Record entity and jurisdiction, department/role scope, reporting and planning periods, as-of date, currency and FX policy, accounting basis, close status, employment/contractor model, service or capacity decision, owner, and approval date.

Route broad savings scans to `profit-improvement`, weekly affordability to `thirteen-week-cash-flow`, and seasonal workforce orchestration to `peak-season-planning`. Keep owner wages/guaranteed payments, distributions, employee payroll, contractors, and agencies separate because their accounting and tax treatment can differ.

## Evidence Gate

Create a source register with `input`, `source`, `extract date`, `covered period`, `entity/department grain`, `coverage`, and limitation. Use aggregated or deidentified payroll data unless individual detail is essential and authorized. Label each value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero.

Separate actual headcount/payroll, approved forecast, and scenario. Tie actual payroll and benefits to closed payroll registers and the general ledger; tie contractors/agencies to AP or contracts and capacity drivers to operational systems.

Use user-defined materiality. Without it, show all payroll and plan variances. If compensation, burden, start date, ramp, capacity, contribution, or cash reserve evidence is insufficient, provide break-even requirements and missing inputs without declaring a hire affordable.

## Workforce Model

Model each role by start/end date and partial month. Define signs once: costs are displayed positive and subtracted in profit/cash views.

- `recurring loaded cash cost[period] = wages + employer payroll taxes + benefits + bonus/commission + expected overtime + recurring tools/equipment + other named recurring employment costs`.
- `first-year cash cost = sum of recurring loaded cash cost for the first 12 months + recruiting + signing + onboarding + training + nonrecurring equipment + other named setup costs`.
- `incremental contribution required = recurring loaded cost`; `incremental net revenue required = recurring loaded cost / applicable contribution margin %` when that margin is positive and consistently defined.
- `cash headroom after hire = scenario ending available cash - approved minimum cash reserve` by period.
- `capacity gap = forecast workload - effective capacity`, with effective capacity reflecting start date, ramp, leave, service level, and utilization assumptions.

Build at least current-plan, delay/alternative, and downside cases. Compare permanent hire, fractional support, contractor/agency, process redesign, and automation where operationally credible. Hiring triggers must be measurable—such as sustained workload, backlog, service level, close workload, margin, or cash headroom—not a date alone.

Do not use revenue per employee as the sole productivity test. Show role-specific throughput, quality/service, manager capacity, control coverage, and the consequence of delay. Keep owner compensation scenarios separate and refer entity-specific tax treatment to a qualified advisor.

## Deliverable

Return:

1. Current workforce and capacity baseline by department/role, with source coverage and reconciliation.
2. Monthly headcount, loaded payroll, contractor/agency, profit, and cash plan with actual/forecast/scenario separated.
3. Role-level trigger, ramp, capacity, affordability, downside, and delay/alternative comparison.
4. A staged recommendation with owner, approval, latest decision date, required evidence, service/control guardrails, and rollback or review point.
5. Source register, variance report, unavailable inputs, and privacy notes.

## Quality Gate

- Tie actual headcount, payroll, benefits, and contractors to control totals without exposing unnecessary PII.
- Reperform loaded-cost, partial-period, capacity, and affordability calculations.
- Confirm no role or cost is duplicated across employee, contractor, agency, and owner categories.
- Confirm actual, forecast, and scenario are separate and no unavailable burden or benefit is treated as zero.
- Confirm the recommendation considers service, quality, controls, management load, legal constraints, and downside cash—not financial ratios alone.

## Guardrails

Stage plans and recommendations only. Never hire, terminate, change pay, classify a worker, run payroll, alter benefits, contact candidates/employees, post/send plans, change access, or move cash without approval. Do not infer protected traits or expose personal payroll data. Obtain qualified HR/employment counsel for workforce actions and CPA/tax review for payroll, worker classification, and owner compensation where required.
