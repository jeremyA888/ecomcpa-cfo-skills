---
name: demand-planning
description: "Connect ecommerce demand forecasts to inventory purchasing, cash planning, SKU replenishment, stockout risk, and overstock decisions. Use when the user mentions demand planning, purchase order timing, inventory forecast, stockouts, overstock, launch quantities, or reorder planning."
---

# Demand Planning

Turn expected sales into purchasing and cash decisions.

## Start Here

Read `.agents/ecom-finance.md` if it exists. Gather historical units sold, current inventory, open POs, lead times, minimum order quantities, supplier terms, seasonality, launches, promos, and sales forecast.

## Planning Logic

- Forecast units by SKU/channel/month.
- Add seasonality, launch, and promo adjustments.
- Compare to on-hand, committed, inbound, and safety stock.
- Calculate reorder point and reorder quantity.
- Map deposits, final payments, freight, and duties into cash forecast.

## Watchouts

Growth can consume cash before profit appears. Stockouts create lost sales; overstock creates trapped cash.

## Output

Return SKU-level risk list, recommended purchase timing, cash impact, and assumptions to verify with operations.
