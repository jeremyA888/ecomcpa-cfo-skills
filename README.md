# EcomCPA CFO Skills for AI Agents

[![Validate skills](https://github.com/jeremyA888/ecomcpa-cfo-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/jeremyA888/ecomcpa-cfo-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Decision-grade agent workflows for ecommerce finance: cash, forecasting, reporting, inventory, margin, working capital, financing, controls, and capital packages.

These 20 skills are designed to make an agent behave like a careful finance operator, not a confident autocomplete. Each workflow requires a defined decision, source lineage, dated coverage, explicit formulas, labeled assumptions, control checks, and a review-gated deliverable. Missing data stays missing; it never silently becomes zero.

## Install

Install the complete pack with the Agent Skills CLI:

```bash
npx skills add jeremyA888/ecomcpa-cfo-skills
```

Inspect the catalog or install selected skills:

```bash
npx skills add jeremyA888/ecomcpa-cfo-skills --list
npx skills add jeremyA888/ecomcpa-cfo-skills --skill thirteen-week-cash-flow financing-strategy product-margin
```

For Claude Code, add this repository as a marketplace, then install the namespaced plugin:

```text
/plugin marketplace add jeremyA888/ecomcpa-cfo-skills
/plugin install ecomcpa-cfo-skills@ecomcpa-cfo-skills
```

Or, from the target project's root, clone to a temporary source directory and copy the skill folders into any client that supports the portable Agent Skills format:

```bash
ECOMCPA_SKILLS_SOURCE="$(mktemp -d)/ecomcpa-cfo-skills"
git clone https://github.com/jeremyA888/ecomcpa-cfo-skills.git "$ECOMCPA_SKILLS_SOURCE"
mkdir -p .agents/skills
cp -R "$ECOMCPA_SKILLS_SOURCE/skills/." .agents/skills/
```

## Start With Governed Context

`ecom-finance-context` can create `.agents/ecom-finance.md`, a small reusable map of the business, finance stack, reporting conventions, metric definitions, priorities, and known data gaps. Other skills read it when present, but they treat it as context—not as current-period evidence.

Before writing that file, confirm the repository's visibility and what the user approves storing. Never put credentials, bank or card numbers, employee-level compensation, customer-level records, raw financial statements, or other sensitive source data in it.

## Choose the Right Skill

| Skill | Primary job | Decision-grade deliverable |
| --- | --- | --- |
| [ecom-finance-context](skills/ecom-finance-context/) | Govern durable brand-finance context | Dated context, definitions, source register, and open questions |
| [accounting-quality-audit](skills/accounting-quality-audit/) | Decide which uses the books can support | Use-case readiness matrix, exceptions, evidence, and remediation gates |
| [thirteen-week-cash-flow](skills/thirteen-week-cash-flow/) | Manage tactical weekly liquidity | Controlled direct-method forecast, variance bridge, low point, and dated actions |
| [cash-flow-forecast](skills/cash-flow-forecast/) | Model strategic monthly runway | Scenario forecast, liquidity risks, sensitivities, and management decisions |
| [budget-forecast](skills/budget-forecast/) | Build or reforecast the operating plan | Driver model, scenario assumptions, variance bridge, and decision register |
| [financial-reporting](skills/financial-reporting/) | Explain verified results to management or a board | Sourced pack with actual/forecast separation, variances, risks, and decisions |
| [kpi-dashboard](skills/kpi-dashboard/) | Govern metric definitions and dashboard design | Metric dictionary, lineage, thresholds, layout, and ownership |
| [inventory-cogs](skills/inventory-cogs/) | Reconcile inventory accounting and COGS | GL/subledger/physical bridges, policy exceptions, and review-gated entry drafts |
| [product-margin](skills/product-margin/) | Diagnose historical SKU economics | Covered-population margin waterfall, rankings, and evidence limits |
| [channel-profitability](skills/channel-profitability/) | Compare economics by channel or fulfillment path | Channel waterfall, allocation sensitivity, confidence, and decisions |
| [pricing-profitability](skills/pricing-profitability/) | Test forward price, promo, bundle, or shipping policy | Bounded scenarios, break-even math, risks, and experiment plan |
| [demand-planning](skills/demand-planning/) | Turn demand into replenishment and purchase timing | SKU risks, order plan, service assumptions, and cash timing |
| [peak-season-planning](skills/peak-season-planning/) | Orchestrate finance for a defined peak event | Integrated scenarios, trigger-owned risk register, cadence, and closeout |
| [working-capital](skills/working-capital/) | Improve structural cash conversion | Defined DIO/DSO/DPO/CCC, quantified levers, and constraint-aware actions |
| [financing-strategy](skills/financing-strategy/) | Choose cash, partial financing, or a capital structure | Funding scenarios, all-in cost, liquidity/downside test, and recommended mix |
| [staffing-plan](skills/staffing-plan/) | Test headcount capacity and affordability | Loaded-cost plan, ramp, downside cash, and hiring triggers |
| [profit-improvement](skills/profit-improvement/) | Prioritize validated profit levers | Non-overlapping EBITDA/cash action portfolio with owners and confidence |
| [lender-investor-package](skills/lender-investor-package/) | Stage evidence for a lender or investor | Audience-specific package, reconciliations, claims register, and open items |
| [internal-controls](skills/internal-controls/) | Design or test finance controls | Risk-control matrix, evidence, exceptions, residual risk, and ownership |
| [finance-tech-stack](skills/finance-tech-stack/) | Select or audit finance-system architecture | Requirements map, current-source scorecard, TCO, migration, and rollback risks |

### Routing boundaries that matter

- Use `thirteen-week-cash-flow` for dated weekly receipts and disbursements; use `cash-flow-forecast` for strategic monthly runway.
- Use `financing-strategy` to choose cash, partial financing, or an instrument; use `lender-investor-package` to assemble materials after the financing path is selected.
- Use `inventory-cogs` to reconcile the inventory records; use `product-margin` to analyze historical SKU economics; use `pricing-profitability` to test a future commercial change.
- Use `accounting-quality-audit` to establish whether data is usable; use `internal-controls` to assess how a process prevents or detects error and fraud.
- Use `kpi-dashboard` to govern definitions and layout; use `financial-reporting` to explain a period's verified results.
- Use specialist skills to quantify individual levers, then use `profit-improvement` to create a non-overlapping action portfolio.

## The Shared Quality Contract

Every analytical skill follows the same controls:

1. Establish the entity, period or as-of date, currency, accounting basis or policy, close status, grain, and decision.
2. Record each source, extract date, coverage, and reconciliation status. Label key values `reported`, `calculated`, `assumption`, or `unavailable`.
3. Separate actuals, forecasts, and scenarios. State formulas, sign conventions, allocations, and company-policy choices.
4. Reconcile to source control totals and quantify open differences. Use management's materiality threshold; if none is supplied, show the variance without inventing one.
5. Return a useful partial result when possible, but do not issue a decision-grade conclusion when critical evidence is missing.
6. Stage work for review. Never post entries, move money, change access, submit financing materials, or send externally without explicit authorization.

If a spreadsheet, document, or presentation is requested, pair the finance skill with the client's file-format skill. The CFO skill controls the finance logic; the file-format skill controls rendering and file integrity.

## Validate the Pack

The repository ships a dependency-free validator plus routing/coexistence and numeric/missing-evidence behavior corpora. All included cases follow a [synthetic-only data boundary](evals/README.md):

```bash
python3 scripts/validate_skills.py
npx skills add . --list
claude plugin validate . --strict
claude plugin validate ./skills --strict
```

The validator checks Agent Skills metadata, the shared finance controls, links, manifests, catalog parity, unfinished placeholders, positive plus boundary routing coverage for every skill, and observable numeric/missing-evidence assertions for high-risk workflows. CI runs it on every pull request and push to `main`.

See [CONTRIBUTING.md](CONTRIBUTING.md) before changing triggers, formulas, safety boundaries, or outputs.

## Professional Boundary

These skills prepare analysis, workpapers, questions, and draft decision support. They do not provide assurance, make management decisions, replace a licensed CPA, tax advisor, attorney, investment professional, or lender, or authorize an agent to act in financial systems. Accounting policy, regulated advice, financing disclosures, and external reporting require the appropriate qualified review.

## License

[MIT](LICENSE) © 2026 EcomCPA.
