#!/usr/bin/env python3
"""Run pinned, no-model-call validation for Claude Code and Codex installs."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
SKILLS_VERSION = "1.5.23"
CLAUDE_CODE_VERSION = "2.1.241"
CODEX_CLI_VERSION = "0.149.1"
RELEASE_VERSION = "0.4.0"
MINIMUM_NODE = (22, 20, 0)
COMMAND_TIMEOUT_SECONDS = 180


class ValidationError(RuntimeError):
    """A deterministic client check failed."""


def executable(name: str) -> str:
    found = shutil.which(name) or shutil.which(f"{name}.cmd")
    if not found:
        raise ValidationError(f"required executable not found: {name}")
    return found


def run(command: list[str], cwd: Path, env: Optional[dict[str, str]] = None) -> None:
    print("+", " ".join(command), flush=True)
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            check=False,
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise ValidationError(
            f"command timed out after {COMMAND_TIMEOUT_SECONDS}s: {' '.join(command)}"
        ) from exc
    if result.returncode:
        raise ValidationError(f"command exited {result.returncode}: {' '.join(command)}")


def output(command: list[str], cwd: Path, env: Optional[dict[str, str]] = None) -> str:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=COMMAND_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        raise ValidationError(
            f"command timed out after {COMMAND_TIMEOUT_SECONDS}s: {' '.join(command)}"
        ) from exc
    if result.returncode:
        raise ValidationError(result.stderr.strip() or f"command failed: {' '.join(command)}")
    return result.stdout


def json_output(
    command: list[str], cwd: Path, env: Optional[dict[str, str]] = None
) -> dict[str, object]:
    raw = output(command, cwd, env)
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"command returned invalid JSON: {' '.join(command)}") from exc
    if not isinstance(parsed, dict):
        raise ValidationError(f"command returned a non-object JSON result: {' '.join(command)}")
    return parsed


def check_node(node: str) -> None:
    raw = output([node, "--version"], ROOT).strip().removeprefix("v")
    try:
        version = tuple(int(part) for part in raw.split(".")[:3])
    except ValueError as exc:
        raise ValidationError(f"could not parse Node version {raw!r}") from exc
    if version < MINIMUM_NODE:
        required = ".".join(str(part) for part in MINIMUM_NODE)
        raise ValidationError(f"Node {required} or newer is required; found {raw}")


def tree_digest(root: Path) -> dict[str, str]:
    if not root.is_dir():
        raise ValidationError(f"missing installed skill directory: {root}")
    digest: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValidationError(f"copy install produced a symlink: {path}")
        if path.is_file():
            relative = path.relative_to(root).as_posix()
            digest[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest


def validate_install(temp_root: Path, npx: str, git: str, safe_env: dict[str, str]) -> None:
    run([git, "init", "--quiet"], temp_root)
    run(
        [
            npx,
            "--yes",
            f"skills@{SKILLS_VERSION}",
            "add",
            str(ROOT),
            "--agent",
            "codex",
            "--agent",
            "claude-code",
            "--skill",
            "*",
            "--copy",
            "--yes",
        ],
        temp_root,
        safe_env,
    )

    source_names = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    source_digest = tree_digest(ROOT / "skills")
    for relative in (Path(".agents/skills"), Path(".claude/skills")):
        installed = temp_root / relative
        installed_names = {path.parent.name for path in installed.glob("*/SKILL.md")}
        if installed_names != source_names:
            raise ValidationError(
                f"{relative} skill set differs: expected={sorted(source_names)}, actual={sorted(installed_names)}"
            )
        if tree_digest(installed) != source_digest:
            raise ValidationError(f"{relative} is not byte-for-byte identical to skills/")

    lock_path = temp_root / "skills-lock.json"
    if not lock_path.is_file():
        raise ValidationError("combined install did not create skills-lock.json")
    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"invalid skills-lock.json: {exc}") from exc
    locked_names = set(lock.get("skills", {}))
    if lock.get("version") != 1 or locked_names != source_names:
        raise ValidationError("skills-lock.json does not cover the complete source catalog")

    sentinel_name = "unrelated-project-skill"
    for relative in (Path(".agents/skills"), Path(".claude/skills")):
        sentinel = temp_root / relative / sentinel_name / "SKILL.md"
        sentinel.parent.mkdir(parents=True, exist_ok=True)
        sentinel.write_text("---\nname: unrelated-project-skill\ndescription: Preserve me.\n---\n")
    run(
        [
            npx,
            "--yes",
            f"skills@{SKILLS_VERSION}",
            "remove",
            *sorted(source_names),
            "--yes",
        ],
        temp_root,
        safe_env,
    )
    for relative in (Path(".agents/skills"), Path(".claude/skills")):
        remaining = {
            path.parent.name for path in (temp_root / relative).glob("*/SKILL.md")
        }
        if remaining != {sentinel_name}:
            raise ValidationError(
                f"named removal was not scoped safely in {relative}: remaining={sorted(remaining)}"
            )


def validate_native_codex(
    temp_root: Path, npx: str, git: str, safe_env: dict[str, str]
) -> None:
    """Exercise Codex's native marketplace on an ephemeral CI runner."""
    marketplace = "ecomcpa-cfo-skills"
    selector = f"{marketplace}@{marketplace}"
    codex = [npx, "--yes", f"@openai/codex@{CODEX_CLI_VERSION}", "plugin"]
    marketplace_added = False
    plugin_added = False

    run([git, "init", "--quiet"], temp_root)
    existing = json_output(
        codex + ["marketplace", "list", "--json"], temp_root, safe_env
    )
    existing_names = {
        item.get("name")
        for item in existing.get("marketplaces", [])
        if isinstance(item, dict)
    }
    if marketplace in existing_names:
        raise ValidationError(f"native Codex smoke requires a clean marketplace name: {marketplace}")

    try:
        run(
            codex + ["marketplace", "add", str(ROOT), "--json"],
            temp_root,
            safe_env,
        )
        marketplace_added = True

        marketplaces = json_output(
            codex + ["marketplace", "list", "--json"], temp_root, safe_env
        )
        added = [
            item
            for item in marketplaces.get("marketplaces", [])
            if isinstance(item, dict) and item.get("name") == marketplace
        ]
        if len(added) != 1:
            raise ValidationError(f"Codex did not register exactly one {marketplace} marketplace")

        result = json_output(
            codex + ["add", selector, "--json"], temp_root, safe_env
        )
        plugin_added = True
        if result.get("pluginId") != selector or result.get("version") != RELEASE_VERSION:
            raise ValidationError(f"Codex install result did not identify {selector} at {RELEASE_VERSION}")
        installed = json_output(codex + ["list", "--json"], temp_root, safe_env)
        matches = [
            item
            for item in installed.get("installed", [])
            if isinstance(item, dict) and item.get("pluginId") == selector
        ]
        if len(matches) != 1 or matches[0].get("version") != RELEASE_VERSION:
            raise ValidationError(
                f"Codex did not install exactly one {selector} at {RELEASE_VERSION}"
            )
    finally:
        if plugin_added:
            run(codex + ["remove", selector, "--json"], temp_root, safe_env)
        if marketplace_added:
            run(
                codex + ["marketplace", "remove", marketplace, "--json"],
                temp_root,
                safe_env,
            )
        if plugin_added:
            remaining_plugins = json_output(
                codex + ["list", "--json"], temp_root, safe_env
            )
            if any(
                isinstance(item, dict) and item.get("pluginId") == selector
                for item in remaining_plugins.get("installed", [])
            ):
                raise ValidationError(f"Codex cleanup left {selector} installed")
        if marketplace_added:
            remaining_marketplaces = json_output(
                codex + ["marketplace", "list", "--json"], temp_root, safe_env
            )
            if any(
                isinstance(item, dict) and item.get("name") == marketplace
                for item in remaining_marketplaces.get("marketplaces", [])
            ):
                raise ValidationError(f"Codex cleanup left {marketplace} configured")


def main() -> int:
    try:
        node = executable("node")
        npx = executable("npx")
        git = executable("git")
        check_node(node)
        safe_env = os.environ.copy()
        safe_env["DO_NOT_TRACK"] = "1"
        safe_env["DISABLE_TELEMETRY"] = "1"

        before = output([git, "status", "--porcelain=v1", "--untracked-files=all"], ROOT)
        run([sys.executable, "scripts/check_public_repo.py"], ROOT, safe_env)
        run([sys.executable, "scripts/validate_skills.py"], ROOT, safe_env)
        run([npx, "--yes", f"skills@{SKILLS_VERSION}", "add", ".", "--list"], ROOT, safe_env)
        run(
            [
                npx,
                "--yes",
                f"@anthropic-ai/claude-code@{CLAUDE_CODE_VERSION}",
                "plugin",
                "validate",
                ".",
                "--strict",
            ],
            ROOT,
            safe_env,
        )
        run(
            [
                npx,
                "--yes",
                f"@anthropic-ai/claude-code@{CLAUDE_CODE_VERSION}",
                "plugin",
                "validate",
                "./skills",
                "--strict",
            ],
            ROOT,
            safe_env,
        )
        with tempfile.TemporaryDirectory(prefix="ecomcpa-cfo-client-smoke-") as temporary:
            validate_install(Path(temporary), npx, git, safe_env)
        if os.environ.get("CI", "").lower() in {"1", "true", "yes"}:
            with tempfile.TemporaryDirectory(prefix="ecomcpa-cfo-codex-smoke-") as temporary:
                validate_native_codex(Path(temporary), npx, git, safe_env)
        after = output([git, "status", "--porcelain=v1", "--untracked-files=all"], ROOT)
        if after != before:
            raise ValidationError("client validation mutated the source checkout")
    except (OSError, ValidationError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("PASS: pinned Claude Code and Codex discovery plus isolated copy installs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
