---
name: inventory-cogs
description: "Reconcile ecommerce inventory units/value, COGS, landed cost, returns, shrinkage, freight, 3PL activity, and inventory accounting. Use for historical GL/subledger/physical-count tie-outs and valuation issues. For future replenishment use demand-planning; for SKU contribution economics use product-margin; for working-capital strategy use working-capital."
license: MIT
---

# Inventory and COGS

Make historical inventory units and value traceable across physical custody, the subledger, and the general ledger.

## Establish the Decision Frame

Read `.agents/ecom-finance.md` if it exists, then state the entity, period and count/as-of date, currency, accounting basis and close status, locations/channels/SKUs, valuation and landed-cost policy, reconciliation purpose, and decision. Record user-defined materiality; if absent, report every variance without silently dismissing one.

Route future units/PO timing to `demand-planning`, SKU contribution economics to `product-margin`, cash-conversion strategy to `working-capital`, and broad book reliability to `accounting-quality-audit`.

## Evidence Gate

Create a source register with `source/report`, `extract or as-of date`, `period/entity/location/SKU coverage`, `units/value control total`, `tie-out status`, and `limitations`. Register beginning/ending GL inventory, subledger snapshots and movements, dated physical/3PL counts, receiving and PO records, supplier/freight/duty invoices, sales/fulfillment quantities, returns disposition, shrink/write-off/sample/owner-use records, and journals.

Label every key value `reported`, `calculated`, `assumption`, or `unavailable`; missing is never zero. Keep actual reconciliation, forecast inventory, and scenarios separate. If beginning/ending control totals, movement detail, cost policy, or cutoff evidence are unavailable, return `Insufficient evidence`, a partial bridge, and the conclusions/entries that cannot be supported.

## Reconciliation and Valuation

Build both unit and value bridges. Choose and state either a gross-return or net-COGS convention; never use both:

`expected ending units = beginning units + receipts + saleable customer returns restored - shipped units - returns to vendor - shrink/write-offs/samples/owner use +/- transfers`

`expected ending value = beginning value + qualifying capitalized receipts/costs + saleable customer returns restored at recorded cost - gross cost of shipped units - returns to vendor at recorded cost - shrink/write-offs/samples/owner use at recorded cost +/- transfers`

If using independently reported GL COGS net of return reversals, omit the separate customer-return restoration and replace gross cost of shipped units with net COGS. Never use COGS as an unexplained plug; if it is derived from ending inventory, say so and do not call the movement a three-way reconciliation. State whether movements are positive additions or positive deductions.

Compare expected ending to the inventory subledger, GL, and dated physical/3PL count separately. Show cutoff and reconciling items by SKU/location/channel; eliminate both sides of transfers at consolidated level. A forced zero variance is not a tie-out.

Apply only costs that qualify under the entity's documented accounting policy and applicable framework. Do not hard-code packaging, outbound freight, fulfillment, abnormal waste, storage, selling, or administrative cost as inventory. Show landed-cost components and allocation formula once, prevent duplication inside COGS, and disclose valuation method, FX treatment, obsolescence/NRV review, and return condition/disposition.

## Deliverable

Return the decision frame and source register, unit bridge, value bridge, subledger-to-GL-to-physical reconciliation, landed-cost/valuation test, issue list, margin/cash implications, and proposed correcting-entry schedule. Each proposed entry must show evidence, accounts, debit/credit sign convention, amount, rationale, uncertainty, and required reviewer; unsupported entries remain unavailable.

## Quality Gate

- Beginning, movement, and ending totals trace to independent registered sources; SKU/location detail sums to disclosed control totals.
- Customer returns, vendor returns, transfers, and net/gross COGS follow one stated convention with no duplication.
- Landed cost is capitalized and recognized once under the documented policy; estimates are not presented as reported cost.
- Actual, forecast, and scenarios remain separate; every variance remains visible unless the user supplies a materiality threshold.
- The reconciliation distinguishes timing/cutoff from quantity, unit-cost, allocation, valuation, and missing-evidence differences.

## Guardrails

Stage reconciliations and entries as drafts only. Never post a journal, adjust inventory, record a write-off, change landed-cost rules, place/alter a PO, send a report, move cash, or change access. Inventory capitalization, valuation, write-off, tax/customs, and correcting-entry decisions require review by the responsible controller or qualified accountant.
