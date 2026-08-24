# EcomCPA CFO Skills for AI Agents

[![Validate skills](https://github.com/jeremyA888/ecomcpa-cfo-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/jeremyA888/ecomcpa-cfo-skills/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Decision-grade agent workflows for ecommerce finance: cash, forecasting, reporting, inventory, margin, working capital, financing, controls, and capital packages.

These 20 skills are designed to make an agent behave like a careful finance operator, not a confident autocomplete. Each workflow requires a defined decision, source lineage, dated coverage, explicit formulas, labeled assumptions, control checks, and a review-gated deliverable. Missing data stays missing; it never silently becomes zero.

## Install

Use one installation method per client. Native plugins are recommended for team distribution; the copied-project method is useful when one private repository must expose the same files to both clients.

Prerequisites: Git, network access to GitHub, and authenticated current versions of Claude Code or Codex. The optional Agent Skills method also requires Node 22.20.0 or newer. Running repository validation additionally requires Python 3.9 or newer. Run project-scoped commands from the intended authorized private repository—not from this public skill-pack checkout.

The native paths follow the official [Claude Code plugin](https://code.claude.com/docs/en/discover-plugins) and [Codex plugin](https://learn.chatgpt.com/docs/build-plugins) formats.

### Claude Code — native plugin

From the target project root:

```bash
claude plugin marketplace add 'https://github.com/jeremyA888/ecomcpa-cfo-skills.git#v0.4.0' --scope project
claude plugin install ecomcpa-cfo-skills@ecomcpa-cfo-skills --scope project
```

In Claude Code, run `/reload-plugins`, then invoke a skill with its plugin namespace:

```text
/ecomcpa-cfo-skills:financing-strategy Compare cash with financing for this order.
```

### Codex — native plugin

Install the exact release from the repository marketplace:

```bash
codex plugin marketplace add jeremyA888/ecomcpa-cfo-skills --ref v0.4.0
codex plugin add ecomcpa-cfo-skills@ecomcpa-cfo-skills
```

Start a new Codex session, use `/skills` to confirm discovery, and invoke the namespaced plugin skill:

```text
$ecomcpa-cfo-skills:financing-strategy Compare cash with financing for this order.
```

### One project copy for both clients

This alternative installs byte copies into `.claude/skills` and `.agents/skills` and creates `skills-lock.json`. The environment variables disable the third-party installer's supported telemetry; GitHub and npm network access is still required.

```bash
DO_NOT_TRACK=1 DISABLE_TELEMETRY=1 npx --yes skills@1.5.23 add \
  'jeremyA888/ecomcpa-cfo-skills#v0.4.0' \
  --agent claude-code \
  --agent codex \
  --skill '*' \
  --copy \
  --yes
```

PowerShell equivalent:

```powershell
$env:DO_NOT_TRACK = "1"
$env:DISABLE_TELEMETRY = "1"
npx --yes skills@1.5.23 add 'jeremyA888/ecomcpa-cfo-skills#v0.4.0' --agent claude-code --agent codex --skill '*' --copy --yes
```

With copied skills, invoke `/financing-strategy` in Claude Code and `$financing-strategy` in Codex. Start new sessions after installation.

Inspect the catalog or install only a deliberate subset:

```bash
DO_NOT_TRACK=1 DISABLE_TELEMETRY=1 npx --yes skills@1.5.23 add \
  'jeremyA888/ecomcpa-cfo-skills#v0.4.0' --list
DO_NOT_TRACK=1 DISABLE_TELEMETRY=1 npx --yes skills@1.5.23 add \
  'jeremyA888/ecomcpa-cfo-skills#v0.4.0' \
  --agent claude-code --agent codex \
  --skill thirteen-week-cash-flow financing-strategy product-margin \
  --copy --yes
```

Do not combine a native plugin with copied folders in the same client. That creates duplicate skill entries and ambiguous update ownership.

### Update or remove

The Claude Code marketplace above is pinned to `v0.4.0`. To move to a later release, uninstall the plugin and remove the marketplace, then repeat the install commands with the new published tag:

```bash
claude plugin uninstall ecomcpa-cfo-skills@ecomcpa-cfo-skills --scope project
claude plugin marketplace remove ecomcpa-cfo-skills --scope project
```

After reinstalling, run `/reload-plugins`.

Codex installs above are pinned to `v0.4.0`. To move to a later release, remove the installed plugin and marketplace, then repeat the two install commands with the new published tag. Removal commands are:

```bash
codex plugin remove ecomcpa-cfo-skills@ecomcpa-cfo-skills
codex plugin marketplace remove ecomcpa-cfo-skills
```

For copied project skills, `DO_NOT_TRACK=1 DISABLE_TELEMETRY=1 npx --yes skills@1.5.23 update --project --yes` refreshes the currently pinned tag; it does not move the project to a newer release. To upgrade, rerun the add command with the new quoted `#vX.Y.Z` source. To remove only this pack without touching unrelated project skills, run this command from the private target project root. Never run the removal block inside this public skill-pack checkout.

```bash
ecomcpa_skills=(
  accounting-quality-audit budget-forecast cash-flow-forecast channel-profitability
  demand-planning ecom-finance-context finance-tech-stack financial-reporting
  financing-strategy internal-controls inventory-cogs kpi-dashboard
  lender-investor-package peak-season-planning pricing-profitability product-margin
  profit-improvement staffing-plan thirteen-week-cash-flow working-capital
)
DO_NOT_TRACK=1 DISABLE_TELEMETRY=1 npx --yes skills@1.5.23 remove \
  "${ecomcpa_skills[@]}" --yes
```

See [TEAM_QUICKSTART.md](TEAM_QUICKSTART.md) for the synthetic acceptance test, privacy boundary, and troubleshooting. The release smoke used Claude Code 2.1.241 and Codex 0.149.0 on macOS; deterministic installation and validation also run on Ubuntu CI. Windows client execution remains explicitly unverified.

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

The repository ships a dependency-free finance validator, a public-repository privacy gate, pinned Claude Code validation, and an isolated two-client installation smoke. All included cases follow a [synthetic-only data boundary](evals/README.md):

```bash
python3 scripts/validate_clients.py
```

That command requires Python 3.9 or newer and Node 22.20.0 or newer, and it runs exact versions `skills@1.5.23` and `@anthropic-ai/claude-code@2.1.241`. It checks Agent Skills metadata, finance controls, links, Claude and Codex manifests, catalog budget, routing coverage, behavior cases, privacy patterns, a generated lock, byte parity, safe named removal, and source-worktree immutability. CI additionally installs the native marketplace with `@openai/codex@0.149.1`, enforces command and job timeouts, and scans reachable Git history with Gitleaks.

The automated behavior corpus validates fixtures and observable assertions; it does not make paid model calls. A release still requires the representative Claude Code and Codex runtime smoke in [TEAM_QUICKSTART.md](TEAM_QUICKSTART.md).

See [CONTRIBUTING.md](CONTRIBUTING.md) before changing triggers, formulas, safety boundaries, or outputs.

## Professional Boundary

These skills prepare analysis, workpapers, questions, and draft decision support. They do not provide assurance, make management decisions, replace a licensed CPA, tax advisor, attorney, investment professional, or lender, or authorize an agent to act in financial systems. Accounting policy, regulated advice, financing disclosures, and external reporting require the appropriate qualified review.

## License

[MIT](LICENSE) © 2026 EcomCPA.
