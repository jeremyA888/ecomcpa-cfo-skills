# Contributing

Contributions are welcome when they make an ecommerce finance workflow more reliable, more discriminating, or easier to use without weakening evidence and authorization boundaries.

## Before You Edit

- Keep one skill focused on one primary finance job-to-be-done.
- Put what the skill does and when it should activate in the frontmatter `description`.
- State overlap boundaries inside the skill: name the neighboring skill and the decision that separates them.
- Add only domain guidance that changes an agent's behavior. Avoid generic finance explanations and decorative process.
- Keep instructions self-contained and under 200 lines. Use `references/` only when conditional detail would otherwise bloat every invocation.
- Preserve the MIT license declaration in each skill.

## Decision-Grade Requirements

Every analytical skill must:

1. Establish entity, period or as-of date, currency, accounting basis or applicable policy, close status, grain, and the decision being supported.
2. Require a source register with extract date, coverage, and reconciliation status.
3. Label key values `reported`, `calculated`, `assumption`, or `unavailable`; missing data must never silently become zero.
4. Separate actuals, forecasts, and scenarios; define formulas, sign conventions, allocations, and policy-dependent classifications.
5. Tie outputs to source control totals, quantify unresolved differences, and avoid inventing a materiality threshold.
6. Define a useful deliverable and an insufficient-evidence path.
7. Stage outputs for review and preserve the no-post, no-send, no-funds-movement, and no-access-change boundaries.

Finance logic must match the company's documented policy. In particular, do not double count landed inventory cost, combine gross margin with variable selling costs, assume blanks are zero, invent covenant definitions, or present unknown customer behavior as a forecast fact.

## Update Routing Evaluations

Any trigger or scope change must update [evals/routing-cases.json](evals/routing-cases.json). Any formula, evidence gate, or authorization change must update [evals/behavior-cases.json](evals/behavior-cases.json). Add realistic positive prompts, coexistence boundaries, and observable assertions that distinguish the intended behavior. Evaluation prompts should contain enough business context to exercise a real decision.

## Validate

Run all repository checks before opening a pull request:

```bash
python3 scripts/validate_clients.py
```

The script uses the Python 3.9-or-newer standard library plus pinned npm client packages and requires Node 22.20.0 or newer. It performs privacy, structure, manifest, catalog, routing, fixture, client-discovery, byte-parity, and source-immutability checks without making model calls. If a required client validator is unavailable, report that check as unrun rather than weakening the gate.

For a changed or substantially expanded skill, also run the [team acceptance smoke](TEAM_QUICKSTART.md) with synthetic data in Claude Code and Codex. Review the resulting artifact—not merely whether a heading or phrase appeared. Verify calculations, source lineage, missing-data behavior, routing, and authorization boundaries.

## Pull Request Checklist

- [ ] The description activates on the intended requests and stays out of neighboring jobs.
- [ ] The workflow contains non-obvious ecommerce finance guidance.
- [ ] Formulas, cost classifications, and metric definitions cannot double count or hide missing coverage.
- [ ] Deliverables identify sources, assumptions, reconciliation status, decisions, owners, and open evidence.
- [ ] No credentials, personal data, customer data, raw client financials, or proprietary client facts are included.
- [ ] The routing corpus and both Claude and Codex plugin manifests are updated when behavior changes.
- [ ] All available validation and forward-use checks pass.
