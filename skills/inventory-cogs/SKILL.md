---
name: inventory-cogs
description: "Reconcile or analyze ecommerce inventory, COGS, landed costs, purchase orders, returns, shrinkage, freight, 3PL activity, SKU margins, and inventory accounting. Use when the user mentions COGS, inventory, landed cost, stockouts, overstock, supplier costs, freight, SKU profitability, or inventory reconciliation."
---

# Inventory and COGS

Make inventory and COGS reliable enough for margin, cash, and forecasting decisions.

## Start Here

Read `.agents/ecom-finance.md` if it exists. Ask for beginning inventory, ending inventory, purchases, freight/duties/tariffs, adjustments, returns, inventory system reports, and sales by SKU.

## Reconciliation Flow

1. Start with beginning inventory from the balance sheet and inventory system.
2. Add purchases, freight-in, duties, tariffs, packaging, and other capitalized landed costs.
3. Subtract COGS, returns to vendor, shrinkage, write-offs, samples, and owner-use items.
4. Tie ending inventory to the balance sheet and inventory subledger.
5. Explain differences by SKU, warehouse, channel, or timing.

## Ecommerce Watchouts

- Marketplace settlements can hide fees and refunds.
- 3PL reports rarely equal accounting inventory without timing review.
- Landed cost must be applied consistently.
- Returns can distort both revenue and inventory.
- Stockouts and overstock are cash-flow problems, not only operations problems.

## Output

Return a reconciliation table, issue list, recommended correcting entries, and a plain-English explanation of how inventory accuracy affects profit and cash.
