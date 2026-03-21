#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:  # pragma: no cover - surfaced to stderr
        fail(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"Missing or invalid front matter in {path.relative_to(ROOT)}")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            fail(f"Malformed front matter line in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def validate_manifests() -> None:
    plugin = load_json(ROOT / ".claude-plugin" / "plugin.json")
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")

    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1:
        fail("Expected exactly one plugin entry in .claude-plugin/marketplace.json")

    market_plugin = plugins[0]

    if plugin.get("name") != marketplace.get("name"):
        fail("plugin.json name does not match marketplace.json name")
    if plugin.get("name") != market_plugin.get("name"):
        fail("plugin.json name does not match marketplace plugin entry name")
    if plugin.get("version") != marketplace.get("metadata", {}).get("version"):
        fail("plugin.json version does not match marketplace metadata.version")
    if market_plugin.get("source") != "./":
        fail("marketplace plugin source should remain './' for repo-root packaging")


def validate_skills() -> list[str]:
    skill_dirs = sorted(
        path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md") if path.is_file()
    )
    if not skill_dirs:
        fail("No shipped skills found in skills/")

    for skill_name in skill_dirs:
        fields = parse_frontmatter(ROOT / "skills" / skill_name / "SKILL.md")
        if fields.get("name") != skill_name:
            fail(
                f"Front matter name mismatch in skills/{skill_name}/SKILL.md: "
                f"expected '{skill_name}', found '{fields.get('name')}'"
            )
        if "description" not in fields:
            fail(f"Missing description in skills/{skill_name}/SKILL.md")

    return skill_dirs


def validate_commands() -> list[str]:
    command_files = sorted((ROOT / "commands").glob("*.md"))
    if not command_files:
        fail("No commands found in commands/")

    commands: list[str] = []
    for path in command_files:
        fields = parse_frontmatter(path)
        if "description" not in fields:
            fail(f"Missing description in {path.relative_to(ROOT)}")
        commands.append(path.stem)
    return commands


def validate_docs(skills: list[str], commands: list[str]) -> None:
    readme = (ROOT / "README.md").read_text()
    claude = (ROOT / "CLAUDE.md").read_text()
    contributing = (ROOT / "CONTRIBUTING.md").read_text()
    changelog = (ROOT / "CHANGELOG.md").read_text()

    for skill in skills:
        if skill not in readme:
            fail(f"README.md does not mention shipped skill '{skill}'")

    for command in commands:
        if f"/{command}" not in readme:
            fail(f"README.md does not mention command '/{command}'")

    if "python3 scripts/validate_repo.py" not in readme:
        fail("README.md should document the validator command")
    if "python3 scripts/validate_repo.py" not in claude:
        fail("CLAUDE.md should document the validator command")
    if "python3 scripts/validate_repo.py" not in contributing:
        fail("CONTRIBUTING.md should document the validator command")
    if "## Unreleased" not in changelog:
        fail("CHANGELOG.md must contain an 'Unreleased' section")


def main() -> None:
    validate_manifests()
    skills = validate_skills()
    commands = validate_commands()
    validate_docs(skills, commands)
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
