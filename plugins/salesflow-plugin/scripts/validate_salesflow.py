#!/usr/bin/env python3
"""Validate the SalesFlow plugin package.

The optional SALESFLOW_BANNED_TERMS env var accepts comma-separated private
terms to scan for without storing those terms in this repository.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

WORKFLOWS = [
    "account-research",
    "communication-summary",
    "followup-draft",
    "daily-briefing",
    "meeting-prep",
    "competitive-brief",
    "pipeline-review",
    "quote-readiness",
]

REQUIRED_FILES = [
    ".codex-plugin/plugin.json",
    "core/capabilities.yaml",
    "core/trigger-map.yaml",
    "core/source-routing.md",
    "core/safety-gates.md",
    "core/tool-contract.openapi.yaml",
    "core/output-schemas/write_plan.json",
    "adapters/codex/USAGE.md",
    "adapters/claude-code/.claude-plugin/plugin.json",
    "adapters/chatgpt/PROJECT_INSTRUCTIONS.md",
    "adapters/chatgpt/actions.openapi.yaml",
    "adapters/synaro/SALESFLOW_WORKFLOW_PACK.md",
    "skills/index/SKILL.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_trigger_map(text: str) -> dict[str, dict[str, list[str]]]:
    workflows: dict[str, dict[str, list[str]]] = {}
    current_workflow: str | None = None
    current_lang: str | None = None
    in_workflows = False

    for raw_line in text.splitlines():
        if raw_line.strip() == "workflows:":
            in_workflows = True
            continue
        if not in_workflows:
            continue

        workflow_match = re.match(r"^  ([a-z0-9-]+):\s*$", raw_line)
        if workflow_match:
            current_workflow = workflow_match.group(1)
            workflows.setdefault(current_workflow, {"zh": [], "en": []})
            current_lang = None
            continue

        lang_match = re.match(r"^    (zh|en):\s*$", raw_line)
        if lang_match and current_workflow:
            current_lang = lang_match.group(1)
            continue

        item_match = re.match(r"^      - [\"']?(.+?)[\"']?\s*$", raw_line)
        if item_match and current_workflow and current_lang:
            workflows[current_workflow][current_lang].append(item_match.group(1))

    return workflows


def validate_manifest() -> None:
    manifest = json.loads(read_text(ROOT / ".codex-plugin/plugin.json"))
    if manifest.get("name") != "salesflow-plugin":
        fail("plugin manifest name must be salesflow-plugin")
    if manifest.get("interface", {}).get("displayName") != "SalesFlow":
        fail("plugin displayName must be SalesFlow")
    prompts = manifest.get("interface", {}).get("defaultPrompt")
    if not isinstance(prompts, list) or len(prompts) != 3:
        fail("plugin defaultPrompt must contain exactly three prompts")


def validate_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    missing.extend(
        [f"skills/{workflow}/SKILL.md" for workflow in WORKFLOWS if not (ROOT / f"skills/{workflow}/SKILL.md").exists()]
    )
    if missing:
        fail("missing required files: " + ", ".join(missing))


def validate_triggers() -> None:
    triggers = parse_trigger_map(read_text(ROOT / "core/trigger-map.yaml"))
    missing = [workflow for workflow in WORKFLOWS if workflow not in triggers]
    if missing:
        fail("missing workflows in trigger-map.yaml: " + ", ".join(missing))
    short = []
    for workflow in WORKFLOWS:
        zh_count = len(triggers[workflow]["zh"])
        en_count = len(triggers[workflow]["en"])
        if zh_count < 3 or en_count < 3:
            short.append(f"{workflow} zh={zh_count} en={en_count}")
    if short:
        fail("each workflow needs at least three zh and three en triggers: " + ", ".join(short))


def validate_write_plan_schema() -> None:
    schema = json.loads(read_text(ROOT / "core/output-schemas/write_plan.json"))
    required = set(schema.get("required", []))
    expected = {
        "workflow_id",
        "target_system",
        "target_object",
        "evidence",
        "proposed_changes",
        "confirmation_status",
        "readback_required",
    }
    missing = sorted(expected - required)
    if missing:
        fail("write_plan schema missing required fields: " + ", ".join(missing))


def validate_forbidden_terms() -> None:
    raw_terms = os.environ.get("SALESFLOW_BANNED_TERMS", "")
    terms = [term.strip() for term in raw_terms.split(",") if term.strip()]
    if not terms:
        return

    checked_suffixes = {".md", ".json", ".yaml", ".yml", ".py"}
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in checked_suffixes:
            continue
        text = read_text(path)
        for term in terms:
            if term.lower() in text.lower():
                hits.append(f"{path.relative_to(ROOT)} contains forbidden term")
    if hits:
        fail("; ".join(hits))


def main() -> None:
    validate_required_files()
    validate_manifest()
    validate_triggers()
    validate_write_plan_schema()
    validate_forbidden_terms()
    print("SalesFlow validation passed.")


if __name__ == "__main__":
    main()
