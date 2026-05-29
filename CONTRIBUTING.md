# Contributing

Contributions are welcome.

## Skill Guidelines

- Keep each skill focused on one ecommerce CFO job-to-be-done.
- Put the trigger terms in the `description` frontmatter, because agents use that field to decide when to load a skill.
- Keep `SKILL.md` practical and concise.
- Do not add tax filing, sales tax, legal, exit advisory, or bookkeeping cleanup workflows to this CFO-only pack unless the project scope changes.
- Use plain language. The intended user may be a finance operator or founder, not a developer.

## Validate Skills

Run an Agent Skills validator against each skill folder before submitting changes. In this local workspace, the current validation command is:

```bash
for d in skills/*; do python3 path/to/quick_validate.py "$d" || exit 1; done
```

Also confirm the plugin JSON files parse:

```bash
python3 -m json.tool .claude-plugin/plugin.json >/dev/null
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
```
