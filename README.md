# EcomCPA CFO Skills for AI Agents

A focused collection of EcomCPA agent skills for ecommerce CFO work. The structure follows one focused skill per job-to-be-done, with a foundation context skill that other skills read first.

These skills are built around the work an ecommerce CFO repeats: cash management, 13-week cash flow, forecasting, financial reporting, KPI dashboards, inventory and COGS analysis, channel profitability, product margin, pricing, staffing, working capital, lender/investor packages, controls, and finance tech stack decisions.

## How Skills Work Together

The `ecom-finance-context` skill is the foundation. It creates `.agents/ecom-finance.md`, which stores the brand's channels, systems, accounting basis, inventory model, cash constraints, debt, goals, KPI targets, and known data-quality issues. Other CFO skills should read that file before asking basic questions.

```
                         ecom-finance-context
                                |
        -------------------------------------------------
        |                  |             |              |
   Cash & Capital     Reporting      Margin Work    Planning
        |                  |             |              |
 13-week-cash-flow   reporting     inventory-cogs   budget-forecast
 cash-flow-forecast  kpi-dashboard product-margin   demand-planning
 working-capital     accounting    channel-profit   staffing-plan
 lender-package      controls      pricing-profit   peak-season
```

## Available Skills

| Skill | What it helps with |
| --- | --- |
| [ecom-finance-context](skills/ecom-finance-context/) | Create or update the shared ecommerce CFO context file. |
| [thirteen-week-cash-flow](skills/thirteen-week-cash-flow/) | Build or update a weekly 13-week cash flow forecast. |
| [cash-flow-forecast](skills/cash-flow-forecast/) | Forecast strategic cash needs across inventory, debt, payroll, and growth. |
| [budget-forecast](skills/budget-forecast/) | Build budgets, reforecasts, and budget-vs-actual operating rhythms. |
| [financial-reporting](skills/financial-reporting/) | Produce CFO-style reporting packs and management commentary. |
| [kpi-dashboard](skills/kpi-dashboard/) | Define ecommerce CFO KPIs and dashboard specs. |
| [accounting-quality-audit](skills/accounting-quality-audit/) | Diagnose whether the numbers are reliable enough for CFO decisions. |
| [inventory-cogs](skills/inventory-cogs/) | Reconcile inventory, landed cost, COGS, returns, and shrinkage for margin decisions. |
| [channel-profitability](skills/channel-profitability/) | Analyze profitability by Shopify, Amazon, retail, wholesale, marketplace, or geography. |
| [product-margin](skills/product-margin/) | Diagnose SKU/product contribution margin and landed-cost issues. |
| [pricing-profitability](skills/pricing-profitability/) | Test price, discount, promo, freight, and margin decisions. |
| [demand-planning](skills/demand-planning/) | Connect sales forecasts to inventory purchasing and cash needs. |
| [working-capital](skills/working-capital/) | Improve cash conversion cycle, AR, AP, inventory turns, and debt usage. |
| [staffing-plan](skills/staffing-plan/) | Plan payroll, hiring, labor capacity, and owner compensation impact. |
| [lender-investor-package](skills/lender-investor-package/) | Build lending, investor, board, or financing packets. |
| [finance-tech-stack](skills/finance-tech-stack/) | Select or audit accounting, inventory, reporting, forecasting, and CFO tools. |
| [internal-controls](skills/internal-controls/) | Strengthen approval, reconciliation, access, fraud, and close controls. |
| [peak-season-planning](skills/peak-season-planning/) | Plan Q4, Prime Day, launches, promos, and seasonal cash/inventory needs. |
| [profit-improvement](skills/profit-improvement/) | Find and prioritize profit leaks across margin, spend, operations, and working capital. |


## Installation

### Option 1: CLI Install

After this repository is published on GitHub, install all skills with:

```bash
npx skills add jeremyA888/ecomcpa-cfo-skills
```

Install specific skills with:

```bash
npx skills add jeremyA888/ecomcpa-cfo-skills --skill thirteen-week-cash-flow cash-flow-forecast kpi-dashboard
```

List available skills with:

```bash
npx skills add jeremyA888/ecomcpa-cfo-skills --list
```

### Option 2: Claude Code Plugin

After this repository is published, add the marketplace and install the plugin:

```bash
/plugin marketplace add jeremyA888/ecomcpa-cfo-skills
/plugin install ecomcpa-cfo-skills
```

### Option 3: Clone and Copy

Copy the skill folders into an agent skills directory:

```bash
git clone https://github.com/jeremyA888/ecomcpa-cfo-skills.git
cd ecomcpa-cfo-skills
cp -r skills/* .agents/skills/
```

For a Claude Code style plugin, use the `.claude-plugin/` metadata in this repo.

## Important Boundary

These skills help an agent organize analysis, workflows, questions, and workpapers for CFO decision-making. They do not replace a licensed CPA, tax advisor, attorney, or other regulated professional when those reviews are required.
