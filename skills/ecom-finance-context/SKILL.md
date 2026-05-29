---
name: ecom-finance-context
description: "Create, update, or read the shared ecommerce CFO context file for an ecommerce brand. Use when the user wants to document CFO context, onboard an agent to a brand's financial model, summarize ecommerce finance operations, define cash/margin/KPI/forecast context, or prepare reusable context for other ecommerce CFO skills."
---

# Ecommerce CFO Context

Create or update `.agents/ecom-finance.md`. This is the foundation file other ecommerce CFO skills should read before asking basic questions.

## Workflow

1. Check for existing context in `.agents/ecom-finance.md`, `.claude/ecom-finance.md`, or obvious finance docs in the repo.
2. Preserve known facts. Mark uncertain items as assumptions or open questions.
3. Keep the file useful for future finance work, not bloated.
4. If the user is non-technical, explain the purpose in plain language.

## Context Template

```markdown
# Ecommerce CFO Context

## Business Snapshot
- Brand:
- Business model:
- Main sales channels:
- Countries/states sold into:
- Growth stage:
- Current finance goal:

## Finance Stack
- Accounting system:
- Inventory system:
- Payroll:
- Banking/credit cards:
- Reporting/BI:

## Accounting Setup
- Accounting basis:
- Close cadence:
- Chart of accounts notes:
- Revenue recognition notes:
- Inventory/COGS method:
- Known data-quality issues:

## Ecommerce Operations
- SKUs/product lines:
- Fulfillment model:
- Warehouses/3PLs:
- Manufacturing/supplier model:
- Returns/discounts/refunds process:
- Marketplace settlement issues:

## CFO Priorities
- Cash constraints:
- Debt/financing:
- Forecasting needs:
- KPI targets:
- Lender/investor/board reporting needs:
- Margin improvement opportunities:
- Working capital constraints:

## Open Questions
- 
```

## Related Skills

Use this before `thirteen-week-cash-flow`, `cash-flow-forecast`, `inventory-cogs`, `channel-profitability`, `budget-forecast`, `lender-investor-package`, and `profit-improvement`.
