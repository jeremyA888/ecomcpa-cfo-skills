#!/usr/bin/env python3
"""Fail closed on common secrets, personal data, and business-data artifacts."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAX_TEXT_BYTES = 1_000_000
ALLOWED_AGENT_FILE = Path(".agents/plugins/marketplace.json")
FORBIDDEN_SUFFIXES = {
    ".csv",
    ".db",
    ".key",
    ".p12",
    ".pdf",
    ".pem",
    ".pfx",
    ".sqlite",
    ".sqlite3",
    ".tsv",
    ".xls",
    ".xlsx",
    ".zip",
}


def pattern(label: str, expression: bytes, flags: int = 0) -> tuple[str, re.Pattern[bytes]]:
    return label, re.compile(expression, flags)


CONTENT_PATTERNS = [
    pattern(
        "private key material",
        b"-----BEGIN " + b"(?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    ),
    pattern("AWS access key", b"\\bAK" + b"IA[A-Z0-9]{16}\\b"),
    pattern("GitHub token", b"\\bgh" + b"[pousr]_[A-Za-z0-9]{20,}\\b"),
    pattern("OpenAI token", b"\\bsk-" + b"(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}\\b"),
    pattern("Slack token", b"\\bxox" + b"[abprs]-[A-Za-z0-9-]{10,}\\b"),
    pattern("Stripe secret", b"\\bsk_" + b"(?:live|test)_[A-Za-z0-9]{16,}\\b"),
    pattern(
        "assigned credential",
        b"\\b(?:api[_-]?key|client[_-]?secret|password|token)\\s*[:=]\\s*"
        + b"[\"']?[A-Za-z0-9+/=_-]{12,}",
        re.IGNORECASE,
    ),
    pattern(
        "email address",
        b"\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}\\b",
        re.IGNORECASE,
    ),
    pattern("macOS user path", b"/Users/" + b"[A-Za-z0-9._-]+/"),
    pattern("Windows user path", b"[A-Za-z]:\\\\Users\\\\" + b"[^\\s\\\\/]+", re.IGNORECASE),
    pattern("US Social Security number", b"\\b[0-9]{3}-" + b"[0-9]{2}-[0-9]{4}\\b"),
    pattern(
        "bank routing number",
        b"\\brouting(?: number)?\\s*[:#=-]?\\s*" + b"[0-9]{9}\\b",
        re.IGNORECASE,
    ),
    pattern("private IPv4 address", b"\\b(?:10\\.|192\\.168\\.|172\\.(?:1[6-9]|2[0-9]|3[01])\\.)"),
]


def run_git(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(message or f"git {' '.join(args)} failed")
    return result.stdout


def candidate_files() -> list[Path]:
    raw = run_git("ls-files", "--cached", "--others", "--exclude-standard", "-z")
    return sorted(Path(item.decode("utf-8")) for item in raw.split(b"\0") if item)


def path_issues(path: Path) -> list[str]:
    issues: list[str] = []
    lower_name = path.name.casefold()
    lower_parts = tuple(part.casefold() for part in path.parts)
    if path.parts and path.parts[0] == ".agents" and path != ALLOWED_AGENT_FILE:
        issues.append("client-generated .agents content")
    if path.parts and path.parts[0] == ".claude":
        issues.append("client-generated .claude content")
    if path.parts and path.parts[0] == ".codex":
        issues.append("client-generated .codex content")
    if path == Path("skills-lock.json"):
        issues.append("client-generated skills lock")
    if path.suffix.casefold() in FORBIDDEN_SUFFIXES:
        issues.append(f"business-data or secret-prone file type {path.suffix}")
    if lower_name == ".env" or lower_name.startswith(".env."):
        issues.append("environment secret file")
    if lower_name.startswith("credentials") and lower_name.endswith(".json"):
        issues.append("credential file")
    if lower_name.startswith("service-account") and lower_name.endswith(".json"):
        issues.append("service-account file")
    if "__pycache__" in lower_parts or lower_name == ".ds_store":
        issues.append("local generated file")
    return issues


def content_issues(path: Path, data: bytes) -> list[str]:
    issues: list[str] = []
    if len(data) > MAX_TEXT_BYTES:
        issues.append(f"file exceeds {MAX_TEXT_BYTES} bytes and requires explicit review")
        return issues
    if b"\0" in data:
        issues.append("binary content requires explicit privacy review")
        return issues
    for label, compiled in CONTENT_PATTERNS:
        if compiled.search(data):
            issues.append(label)
    return issues


def metadata_issues() -> list[str]:
    issues: list[str] = []
    emails = run_git("log", "--all", "--format=%ae%n%ce").decode("utf-8").splitlines()
    exposed = sorted({email for email in emails if email and not email.endswith("@users.noreply.github.com")})
    if exposed:
        issues.append("commit metadata contains an email other than a GitHub noreply address")

    metadata = b"\n".join(
        [
            run_git("log", "--all", "--format=%B"),
            run_git("for-each-ref", "--format=%(refname)%09%(taggername)%09%(taggeremail)"),
        ]
    )
    for label, compiled in CONTENT_PATTERNS:
        if label == "email address":
            continue
        if compiled.search(metadata):
            issues.append(f"Git metadata contains {label}")
    return issues


def main() -> int:
    findings: list[str] = []
    try:
        paths = candidate_files()
        for path in paths:
            for issue in path_issues(path):
                findings.append(f"{path}: {issue}")
            absolute = ROOT / path
            if absolute.is_symlink():
                findings.append(f"{path}: symbolic links require explicit privacy review")
                continue
            if absolute.is_file():
                for issue in content_issues(path, absolute.read_bytes()):
                    findings.append(f"{path}: {issue}")
        findings.extend(metadata_issues())
    except (OSError, RuntimeError) as exc:
        print(f"FAIL: privacy scan could not complete: {exc}", file=sys.stderr)
        return 1

    if findings:
        print(f"FAIL: {len(findings)} public-repository privacy issue(s)", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        print("Matched values are intentionally redacted.", file=sys.stderr)
        return 1

    print(f"PASS: {len(paths)} candidate files and reachable Git metadata passed privacy checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
