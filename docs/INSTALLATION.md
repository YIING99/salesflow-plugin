# Installation

## Codex

```bash
codex plugin marketplace add github:YIING99/salesflow-plugin
codex plugin add salesflow-plugin@salesflow
```

Start a new Codex thread after installation so the new skills are loaded.

## Local Codex Development

```bash
git clone https://github.com/YIING99/salesflow-plugin.git
cd salesflow-plugin
codex plugin marketplace add .
codex plugin add salesflow-plugin@salesflow
```

## Claude Code

Install from the GitHub marketplace:

```bash
claude plugin marketplace add YIING99/salesflow-plugin
claude plugin install salesflow-plugin@salesflow
```

For manual review or adapter reuse, the Claude Code adapter lives under:

```text
plugins/salesflow-plugin/adapters/claude-code/
```

## ChatGPT

Copy the Project Instructions from:

```text
plugins/salesflow-plugin/adapters/chatgpt/PROJECT_INSTRUCTIONS.md
```

If Actions are available, use:

```text
plugins/salesflow-plugin/adapters/chatgpt/actions.openapi.yaml
```

## Synaro Or Generic Agents

Use:

```text
plugins/salesflow-plugin/adapters/synaro/SALESFLOW_WORKFLOW_PACK.md
```
