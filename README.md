# SalesFlow

Open-source bilingual sales workflow plugin for Codex, Claude Code, ChatGPT, and Synaro.

SalesFlow turns everyday sales requests into evidence-grounded workflows:
customer research, conversation summaries, follow-up drafts, daily sales briefings,
meeting prep, competitive briefs, pipeline reviews, and quote readiness checks.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Codex Plugin](https://img.shields.io/badge/Codex-plugin-blue.svg)](plugins/salesflow-plugin/.codex-plugin/plugin.json)
[![Bilingual](https://img.shields.io/badge/Triggers-English%20%2B%20Chinese-purple.svg)](plugins/salesflow-plugin/core/trigger-map.yaml)

## Why SalesFlow

Most sales agents fail in the same places:

- They confuse raw evidence with CRM truth.
- They write to durable systems before the user confirms.
- They mix customer-specific notes with reusable sales knowledge.
- They draft customer emails without showing the evidence boundary.

SalesFlow fixes that by enforcing a simple sequence:

```text
evidence -> identity check -> fact/judgment split -> seller artifact -> write plan -> user confirmation -> readback
```

## Core Workflows

| Workflow | Chinese triggers | English triggers |
| --- | --- | --- |
| `account-research` | 客户背调, 客户调研, 查客户, 查公司, 客户画像 | account research, company research, customer profile |
| `communication-summary` | 沟通复盘, 通话总结, 邮件归档, 对话归档, 提炼线索 | call summary, meeting recap, extract sales notes |
| `followup-draft` | 起草邮件, 写回复, 跟进邮件, 客户回复 | draft follow-up, draft outreach, follow-up email |
| `daily-briefing` | 销售早报, 今日跟进, 今天先跟谁 | daily briefing, today's follow-ups, sales briefing |
| `meeting-prep` | 会前准备, 客户会议准备, 拜访准备 | meeting prep, call prep, prepare for customer meeting |
| `competitive-brief` | 竞品分析, 竞品话术, 异议处理, 反驳话术 | competitive brief, battlecard, objection handling |
| `pipeline-review` | 销售看板复盘, 周会复盘, 客户跟进复盘 | pipeline review, account review, weekly sales review |
| `quote-readiness` | 报价准备, 报价前检查, 报价资料检查 | quote readiness, quote prep, quotation check |

## Install In Codex

Install directly from GitHub as a local marketplace:

```bash
codex plugin marketplace add github:YIING99/salesflow-plugin
codex plugin add salesflow-plugin@salesflow
```

For local development:

```bash
git clone https://github.com/YIING99/salesflow-plugin.git
cd salesflow-plugin
codex plugin marketplace add .
codex plugin add salesflow-plugin@salesflow
python3 plugins/salesflow-plugin/scripts/validate_salesflow.py
```

## Use With Other Agents

- Codex: use `plugins/salesflow-plugin/.codex-plugin/plugin.json`.
- Claude Code: use `plugins/salesflow-plugin/adapters/claude-code/`.
- ChatGPT: copy `plugins/salesflow-plugin/adapters/chatgpt/PROJECT_INSTRUCTIONS.md` and optionally expose the Actions schema.
- Synaro or generic agents: use `plugins/salesflow-plugin/adapters/synaro/SALESFLOW_WORKFLOW_PACK.md`.

## Optional Memory Integrations

SalesFlow is vendor-neutral. It can work with pasted notes, files, CRM exports, or any knowledge base.

For teams that want persistent AI memory:

- [KnowSales](https://www.knowsales.ai) can act as the sales memory layer for customer profiles, activities, product knowledge, objection handling, and competitor intelligence.
- [KnowMine](https://knowmine.ai) can act as the personal or team learning layer for reusable judgment, preferences, and process memory.

These integrations are optional. SalesFlow's core contract uses generic targets such as
`sales_knowledge_base`, `personal_knowledge_base`, `lightweight_tracker`, and `quotation_workflow`.

## Privacy And Safety

SalesFlow is designed for de-identified, source-controlled workflow logic. It does not include:

- private customer records
- internal chat logs
- email transcripts
- browser sessions or login state
- API keys, tokens, secrets, or environment files
- company-specific business rules

Before publishing your own fork, run:

```bash
python3 plugins/salesflow-plugin/scripts/validate_salesflow.py
bash scripts/public_release_audit.sh
```

See [Privacy And Security](docs/PRIVACY_AND_SECURITY.md) for the public-release checklist.

## Repository SEO Keywords

sales workflow plugin, Codex plugin, Claude Code skill, ChatGPT sales automation,
bilingual sales agent, sales AI workflow, CRM write plan, customer follow-up automation,
meeting prep AI, account research AI, sales knowledge base, personal knowledge base,
MCP sales workflow, pipeline review, quote readiness, objection handling.

## License

MIT
