# SalesFlow Workflow Pack For Synaro

## Purpose

SalesFlow routes bilingual sales requests into evidence-grounded workflows and write plans.

## Supported Natural Commands

- 客户背调 / account research
- 沟通复盘 / call summary
- 起草邮件 / draft follow-up
- 销售早报 / daily briefing
- 会前准备 / meeting prep
- 竞品分析 / competitive brief
- 销售看板复盘 / pipeline review
- 报价准备 / quote readiness

## Required Procedure

1. Match the request against `core/trigger-map.yaml`.
2. Collect evidence and classify it by evidence level.
3. Identify customer using hard identifiers before claiming a match.
4. Separate facts, judgments, estimates, and proposed actions.
5. Produce the relevant output template from `core/output-schemas/`.
6. If persistence is needed, produce `write_plan.json`.
7. Wait for user confirmation before durable writes.
8. Read back after writing.

