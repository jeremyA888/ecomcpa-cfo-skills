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
MAX_DESCRIPTION_CHARS = 210
MAX_CATALOG_DESCRIPTION_CHARS = 4200


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

        if not description or len(description) > MAX_DESCRIPTION_CHARS:
            errors.append(
                f"{rel}: description must contain 1-{MAX_DESCRIPTION_CHARS} characters"
            )
        elif "use" not in description.casefold().split():
            errors.append(f"{rel}: description must include explicit Use routing guidance")
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
    total_description_chars = sum(len(text) for text in descriptions)
    if total_description_chars > MAX_CATALOG_DESCRIPTION_CHARS:
        errors.append(
            "skills/: descriptions exceed the cross-client catalog budget "
            f"({total_description_chars}>{MAX_CATALOG_DESCRIPTION_CHARS})"
        )
    return names


def validate_manifests(skill_names: set[str], errors: list[str]) -> None:
    claude_plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    claude_marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    codex_plugin_path = ROOT / ".codex-plugin" / "plugin.json"
    codex_marketplace_path = ROOT / ".agents" / "plugins" / "marketplace.json"
    try:
        claude_plugin = json.loads(claude_plugin_path.read_text(encoding="utf-8"))
        claude_marketplace = json.loads(claude_marketplace_path.read_text(encoding="utf-8"))
        codex_plugin = json.loads(codex_plugin_path.read_text(encoding="utf-8"))
        codex_marketplace = json.loads(codex_marketplace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"plugin manifests: {exc}")
        return

    expected_repo = "https://github.com/jeremyA888/ecomcpa-cfo-skills"
    if claude_plugin.get("skills") != "./skills":
        errors.append(".claude-plugin/plugin.json: skills must point to ./skills")
    if claude_plugin.get("repository") != expected_repo:
        errors.append(".claude-plugin/plugin.json: repository URL is not canonical")

    claude_plugins = claude_marketplace.get("plugins", [])
    if len(claude_plugins) != 1 or claude_plugins[0].get("source") != "./":
        errors.append(".claude-plugin/marketplace.json: expected one root plugin source")
    description = claude_plugins[0].get("description", "") if claude_plugins else ""
    if f"{len(skill_names)} ecommerce CFO skills" not in description:
        errors.append(".claude-plugin/marketplace.json: plugin description has a stale skill count")
    if claude_marketplace.get("description", "") == "":
        errors.append(".claude-plugin/marketplace.json: top-level description is required")

    if codex_plugin.get("name") != "ecomcpa-cfo-skills":
        errors.append(".codex-plugin/plugin.json: canonical name is required")
    if codex_plugin.get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: skills must point to ./skills/")
    if codex_plugin.get("repository") != expected_repo:
        errors.append(".codex-plugin/plugin.json: repository URL is not canonical")
    if codex_plugin.get("author", {}).get("name") != "EcomCPA":
        errors.append(".codex-plugin/plugin.json: author.name must be EcomCPA")

    interface = codex_plugin.get("interface", {})
    required_interface = {
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "websiteURL",
        "defaultPrompt",
    }
    missing_interface = sorted(required_interface - interface.keys())
    if missing_interface:
        errors.append(
            ".codex-plugin/plugin.json: missing interface fields " + ", ".join(missing_interface)
        )
    prompts = interface.get("defaultPrompt", [])
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3:
        errors.append(".codex-plugin/plugin.json: defaultPrompt must contain 1-3 prompts")
    elif any(not isinstance(prompt, str) or len(prompt) > 128 for prompt in prompts):
        errors.append(".codex-plugin/plugin.json: default prompts must be strings of 128 characters or fewer")

    codex_plugins = codex_marketplace.get("plugins", [])
    if codex_marketplace.get("name") != "ecomcpa-cfo-skills":
        errors.append(".agents/plugins/marketplace.json: canonical marketplace name is required")
    if codex_marketplace.get("interface", {}).get("displayName") != "EcomCPA CFO Skills":
        errors.append(".agents/plugins/marketplace.json: displayName is required")
    if len(codex_plugins) != 1:
        errors.append(".agents/plugins/marketplace.json: expected exactly one plugin")
    else:
        entry = codex_plugins[0]
        if entry.get("name") != "ecomcpa-cfo-skills":
            errors.append(".agents/plugins/marketplace.json: plugin name is not canonical")
        if entry.get("source") != {"source": "local", "path": "./"}:
            errors.append(".agents/plugins/marketplace.json: source must resolve to the repository root")
        if entry.get("policy") != {
            "installation": "AVAILABLE",
            "authentication": "ON_INSTALL",
        }:
            errors.append(".agents/plugins/marketplace.json: explicit install policy is required")
        if entry.get("category") != "Productivity":
            errors.append(".agents/plugins/marketplace.json: category must be Productivity")

    versions = [
        claude_plugin.get("version", ""),
        claude_plugins[0].get("version", "") if claude_plugins else "",
        codex_plugin.get("version", ""),
    ]
    if any(not re.fullmatch(r"\d+\.\d+\.\d+", version) for version in versions):
        errors.append("plugin manifests: all versions must use semantic versioning")
    if len(set(versions)) != 1:
        errors.append("plugin manifests: Claude and Codex version values must match")


def validate_readme(skill_names: set[str], errors: list[str]) -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    try:
        release_version = json.loads(
            (ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )["version"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        errors.append(f"README.md: could not derive release version: {exc}")
        release_version = ""
    linked = set(re.findall(r"\(skills/([a-z0-9-]+)/\)", text))
    if linked != skill_names:
        missing = sorted(skill_names - linked)
        extra = sorted(linked - skill_names)
        errors.append(f"README.md: skill catalog mismatch; missing={missing}, extra={extra}")
    if "after this repository is published" in text.casefold():
        errors.append("README.md: still describes the public repository as unpublished")
    required_snippets = {
        "$financing-strategy",
        "/ecomcpa-cfo-skills:financing-strategy",
        "Node 22.20.0",
        "TEAM_QUICKSTART.md",
        "scripts/validate_clients.py",
    }
    missing_snippets = sorted(snippet for snippet in required_snippets if snippet not in text)
    if missing_snippets:
        errors.append(f"README.md: missing client handoff details {missing_snippets}")
    if release_version:
        pinned_source = f"'jeremyA888/ecomcpa-cfo-skills#v{release_version}'"
        if text.count(pinned_source) != 4:
            errors.append(
                "README.md: all four Agent Skills sources must use the quoted # Git-ref pin"
            )
        mistaken_selector = f"jeremyA888/ecomcpa-cfo-skills@v{release_version}"
        if mistaken_selector in text:
            errors.append("README.md: @version is a skill selector, not a Git-ref pin")
        pinned_claude = (
            f"'https://github.com/jeremyA888/ecomcpa-cfo-skills.git#v{release_version}'"
        )
        if pinned_claude not in text:
            errors.append("README.md: Claude marketplace source must pin the release tag")
    check_links(path, text, errors)
    unfinished = UNFINISHED_RE.search(text)
    if unfinished:
        errors.append(f"README.md: unfinished marker {unfinished.group(0)!r}")

    quickstart_path = ROOT / "TEAM_QUICKSTART.md"
    try:
        quickstart = quickstart_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"TEAM_QUICKSTART.md: {exc}")
        return
    check_links(quickstart_path, quickstart, errors)
    for snippet in ("synthetic", "authorized private workspace", "cross-border", "advisory-only"):
        if snippet not in quickstart.casefold():
            errors.append(f"TEAM_QUICKSTART.md: missing required boundary {snippet!r}")


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
        "financing-strategy",
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
