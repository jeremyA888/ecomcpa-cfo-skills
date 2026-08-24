#!/usr/bin/env python3
"""Validate the public skill pack without third-party dependencies."""

from __future__ import annotations

import ast
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
UNFINISHED_RE = re.compile(
    r"(?i)(?:\bTODO\b|\bFIXME\b|\bTBD\b|path/to/quick_validate|example\.com|\[INSERT[^\]]*\])"
)
REQUIRED_HEADINGS = {
    "## Establish the Decision Frame",
    "## Evidence Gate",
    "## Deliverable",
    "## Quality Gate",
    "## Guardrails",
}
STATUS_LABELS = {"reported", "calculated", "assumption", "unavailable"}


def scalar(raw: str) -> str:
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
        try:
            value = ast.literal_eval(raw)
        except (SyntaxError, ValueError):
            return raw[1:-1]
        return value if isinstance(value, str) else str(value)
    return raw


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("must start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError("frontmatter is not closed")

    metadata: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = scalar(value)
    return metadata, parts[2].strip()


def check_links(path: Path, text: str, errors: list[str]) -> None:
    for raw_target in LINK_RE.findall(text):
        target = raw_target.split("#", 1)[0].strip("<>")
        if target and not (path.parent / target).exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {raw_target!r}")


def validate_skills(errors: list[str]) -> set[str]:
    names: set[str] = set()
    descriptions: list[str] = []
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        errors.append("skills/: no SKILL.md files found")
        return names

    for path in skill_files:
        rel = path.relative_to(ROOT)
        try:
            metadata, body = parse_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue

        name = metadata.get("name", "")
        description = metadata.get("description", "")
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{rel}: invalid skill name {name!r}")
        if name != path.parent.name:
            errors.append(f"{rel}: name must match parent directory")
        if name in names:
            errors.append(f"{rel}: duplicate skill name {name!r}")
        names.add(name)

        if not description or len(description) > 1024:
            errors.append(f"{rel}: description must contain 1-1024 characters")
        elif not re.search(r"\buse (?:when|for|to)\b", description.lower()):
            errors.append(f"{rel}: description must say when the skill applies")
        descriptions.append(description.casefold())

        if metadata.get("license") != "MIT":
            errors.append(f"{rel}: frontmatter must declare the MIT license")
        if not body:
            errors.append(f"{rel}: instruction body is empty")
            continue
        if len(body.splitlines()) > 200:
            errors.append(f"{rel}: exceeds 200 lines; move conditional detail to references/")

        missing_headings = sorted(heading for heading in REQUIRED_HEADINGS if heading not in body)
        if missing_headings:
            errors.append(f"{rel}: missing required sections: {', '.join(missing_headings)}")

        lower_body = body.casefold()
        missing_labels = sorted(label for label in STATUS_LABELS if f"`{label}`" not in lower_body)
        if missing_labels:
            errors.append(f"{rel}: missing evidence labels: {', '.join(missing_labels)}")
        if "missing" not in lower_body or "zero" not in lower_body:
            errors.append(f"{rel}: must state that missing data is not zero")
        if "materiality" not in lower_body:
            errors.append(f"{rel}: must define materiality handling")
        if "source" not in lower_body or "as-of" not in lower_body:
            errors.append(f"{rel}: must require source lineage and an as-of date")

        check_links(path, body, errors)
        unfinished = UNFINISHED_RE.search(body)
        if unfinished:
            errors.append(f"{rel}: unfinished marker {unfinished.group(0)!r}")

    duplicate_descriptions = [text for text, count in Counter(descriptions).items() if count > 1]
    if duplicate_descriptions:
        errors.append("skills/: duplicate descriptions weaken skill routing")
    return names


def validate_manifests(skill_names: set[str], errors: list[str]) -> None:
    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"plugin manifests: {exc}")
        return

    if plugin.get("skills") != "./skills":
        errors.append("plugin.json: skills must point to ./skills")
    version = plugin.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("plugin.json: version must use semantic versioning")
    expected_repo = "https://github.com/jeremyA888/ecomcpa-cfo-skills"
    if plugin.get("repository") != expected_repo:
        errors.append("plugin.json: repository URL is not canonical")

    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("source") != "./":
        errors.append("marketplace.json: expected one root plugin source")
    description = plugins[0].get("description", "") if plugins else ""
    if plugins and plugins[0].get("version") != version:
        errors.append("plugin manifests: plugin version values must match")
    if f"{len(skill_names)} ecommerce CFO skills" not in description:
        errors.append("marketplace.json: plugin description has a stale skill count")
    if marketplace.get("description", "") == "":
        errors.append("marketplace.json: top-level description is required")


def validate_readme(skill_names: set[str], errors: list[str]) -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    linked = set(re.findall(r"\(skills/([a-z0-9-]+)/\)", text))
    if linked != skill_names:
        missing = sorted(skill_names - linked)
        extra = sorted(linked - skill_names)
        errors.append(f"README.md: skill catalog mismatch; missing={missing}, extra={extra}")
    if "after this repository is published" in text.casefold():
        errors.append("README.md: still describes the public repository as unpublished")
    check_links(path, text, errors)
    unfinished = UNFINISHED_RE.search(text)
    if unfinished:
        errors.append(f"README.md: unfinished marker {unfinished.group(0)!r}")


def validate_routing_evals(skill_names: set[str], errors: list[str]) -> None:
    path = ROOT / "evals" / "routing-cases.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"evals/routing-cases.json: {exc}")
        return
    if not isinstance(cases, list):
        errors.append("evals/routing-cases.json: top level must be an array")
        return

    ids: set[str] = set()
    expected_coverage: Counter[str] = Counter()
    reject_coverage: Counter[str] = Counter()
    for index, case in enumerate(cases):
        label = f"evals/routing-cases.json[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label}: case must be an object")
            continue
        case_id = case.get("id")
        prompt = case.get("prompt")
        expected = case.get("expected")
        reject = case.get("reject", [])
        reason = case.get("reason")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{label}: missing id")
        elif case_id in ids:
            errors.append(f"{label}: duplicate id {case_id!r}")
        else:
            ids.add(case_id)
        if not isinstance(prompt, str) or len(prompt.split()) < 8:
            errors.append(f"{label}: prompt is not realistic enough")
        if expected not in skill_names:
            errors.append(f"{label}: unknown expected skill {expected!r}")
        else:
            expected_coverage[expected] += 1
        if not isinstance(reject, list) or not reject:
            errors.append(f"{label}: reject must name at least one plausible collision")
            reject = []
        for name in reject:
            if name not in skill_names:
                errors.append(f"{label}: unknown rejected skill {name!r}")
            elif name == expected:
                errors.append(f"{label}: expected skill cannot also be rejected")
            else:
                reject_coverage[name] += 1
        if not isinstance(reason, str) or len(reason.split()) < 4:
            errors.append(f"{label}: reason is too thin")

    missing_expected = sorted(skill_names - expected_coverage.keys())
    missing_rejected = sorted(skill_names - reject_coverage.keys())
    if missing_expected:
        errors.append(f"routing evals: no positive case for {missing_expected}")
    if missing_rejected:
        errors.append(f"routing evals: no coexistence boundary for {missing_rejected}")


def validate_behavior_evals(skill_names: set[str], errors: list[str]) -> None:
    path = ROOT / "evals" / "behavior-cases.json"
    try:
        cases = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"evals/behavior-cases.json: {exc}")
        return
    if not isinstance(cases, list):
        errors.append("evals/behavior-cases.json: top level must be an array")
        return

    ids: set[str] = set()
    coverage: Counter[str] = Counter()
    for index, case in enumerate(cases):
        label = f"evals/behavior-cases.json[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label}: case must be an object")
            continue
        case_id = case.get("id")
        skill = case.get("skill")
        prompt = case.get("prompt")
        assertions = case.get("assertions")
        if not isinstance(case_id, str) or not case_id:
            errors.append(f"{label}: missing id")
        elif case_id in ids:
            errors.append(f"{label}: duplicate id {case_id!r}")
        else:
            ids.add(case_id)
        if skill not in skill_names:
            errors.append(f"{label}: unknown skill {skill!r}")
        else:
            coverage[skill] += 1
        if not isinstance(prompt, str) or len(prompt.split()) < 25:
            errors.append(f"{label}: prompt is not realistic enough")
        if not isinstance(assertions, list) or len(assertions) < 4:
            errors.append(f"{label}: provide at least four observable assertions")
        elif any(not isinstance(item, str) or len(item.split()) < 5 for item in assertions):
            errors.append(f"{label}: assertions must be concrete sentences")

    high_risk = {
        "accounting-quality-audit",
        "cash-flow-forecast",
        "finance-tech-stack",
        "financial-reporting",
        "internal-controls",
        "inventory-cogs",
        "pricing-profitability",
        "product-margin",
        "staffing-plan",
        "thirteen-week-cash-flow",
        "working-capital",
    }
    missing = sorted(high_risk - coverage.keys())
    if missing:
        errors.append(f"behavior evals: no high-risk case for {missing}")


def main() -> int:
    errors: list[str] = []
    skill_names = validate_skills(errors)
    validate_manifests(skill_names, errors)
    validate_readme(skill_names, errors)
    validate_routing_evals(skill_names, errors)
    validate_behavior_evals(skill_names, errors)

    if errors:
        print(f"FAIL: {len(errors)} issue(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(skill_names)} skills, manifests, README, links, routing evals, and behavior evals")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
