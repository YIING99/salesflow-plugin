# Codex Adapter

The root `.codex-plugin/plugin.json` is the Codex manifest for SalesFlow.

## Runtime Rules

1. Load `skills/index/SKILL.md` for broad routing and orientation.
2. Load the focused workflow skill when the user request matches a bilingual trigger.
3. The focused skill must read:
   - `core/trigger-map.yaml`
   - `core/source-routing.md`
   - `core/safety-gates.md`
   - the relevant output schema under `core/output-schemas/`
4. Do not write to durable systems without a `write_plan` and explicit user confirmation.
5. After a write, read back the target object and report what was actually saved.

## Suggested Prompts

- `客户背调：帮我查这个客户并判断下一步怎么跟。`
- `Summarize this customer conversation and draft a follow-up.`
- `今天我应该优先跟进哪些客户？`

