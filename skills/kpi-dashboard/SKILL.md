---
name: kpi-dashboard
description: "Define ecommerce finance KPIs, dashboard specs, metric formulas, targets, and data sources. Use when the user mentions KPI dashboard, ecommerce metrics, finance metrics, LTV, CAC, AOV, inventory turns, gross margin, contribution margin, repeat purchase, or channel ROI."
---

# KPI Dashboard

Define the metrics that show whether the ecommerce business is healthy.

## Start Here

Read `.agents/ecom-finance.md` if it exists. Identify the decision audience: founder, CFO, controller, lender, investor, or operator.

## Core KPIs

- Revenue, net revenue, gross margin, contribution margin.
- CAC, MER, ROAS, marketing efficiency by channel.
- AOV, conversion rate, repeat purchase rate, LTV.
- Refund rate, discount rate, chargeback rate.
- Inventory turns, weeks of supply, stockout risk, aged inventory.
- Cash balance, runway, cash conversion cycle.
- EBITDA, operating income, debt service coverage.

## Dashboard Spec

For each KPI define:

- Formula.
- Source system.
- Refresh cadence.
- Owner.
- Target/threshold.
- Decision it supports.

## Output

Return a KPI dictionary and dashboard layout. Flag vanity metrics and metrics that cannot be trusted until accounting data is cleaned.
