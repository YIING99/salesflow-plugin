---
name: index
description: Use when a user asks for SalesFlow, 销售流, customer research, 客户背调, communication summary, 沟通复盘, follow-up drafts, 销售早报, meeting prep, 竞品分析, pipeline review, or quote readiness in Chinese or English.
---

# SalesFlow Index

SalesFlow is a bilingual sales workflow router. Use it to select one or more focused workflows,
then follow the core gates before producing artifacts or write plans.

## Required Files

Read these before focused work:
- `../../core/trigger-map.yaml`
- `../../core/source-routing.md`
- `../../core/safety-gates.md`

## Routing

If several workflows match, sequence them in this order:
identity and evidence -> account research -> communication summary -> follow-up draft -> write plan.

Never write directly because a trigger matched. Durable writes require `write_plan`, user
confirmation, and readback.

