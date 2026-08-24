# Agent Contributor Guide

This repository packages portable ecommerce CFO skills. Preserve trust before adding breadth.

## Scope

- Keep each skill independently usable; selective installation may copy only one skill folder.
- Preserve existing skill names unless a migration plan is part of the requested change.
- Put trigger and coexistence language in frontmatter. Put runtime finance logic in the body.
- Add a resource only when it changes decisions or provides reusable deterministic mechanics.

## Finance Invariants

- Establish entity, period or as-of date, currency, basis or policy, close status, grain, and decision.
- Track source, extract date, coverage, and reconciliation status. Missing is not zero.
- Label key values `reported`, `calculated`, `assumption`, or `unavailable`.
- Separate actuals, forecasts, and scenarios; show formulas, sign conventions, allocations, and policy choices.
- Reconcile to control totals. Quantify open differences and never invent materiality.
- Do not double count landed cost, variable selling costs, channel receipts, or profit levers.
- Do not call undrawn credit cash or choose financing from headline APR without dated liquidity, all-in cost, downside repayment, collateral, covenant, and guarantee analysis.
- Stage work for review. Never authorize posting, payment, access changes, financing submission, or external sending.

## Data Boundary

Use synthetic data in examples and evaluations. Do not commit credentials, personal data, customer-level data, employee-level compensation, account numbers, raw client financials, or proprietary client facts. Reusable context files contain governed facts and pointers, not source records.

## Required Checks

Run before handing off changes:

```bash
python3 scripts/validate_clients.py
```

The script requires Python 3.9 or newer and Node 22.20.0 or newer. It runs pinned structural, privacy, Claude Code, Codex-discovery, and isolated two-client copy-install checks without model calls. For substantial skill changes, forward-test realistic synthetic prompts in both clients and inspect calculations, missing-data behavior, routing, and authorization—not merely headings. Use [TEAM_QUICKSTART.md](TEAM_QUICKSTART.md) as the release smoke.

Keep the SemVer value identical in both plugin manifests and the Claude marketplace entry. Any published behavioral change requires a version bump; create the matching Git tag when cutting a release.
