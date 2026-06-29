# SalesFlow Project Instructions For ChatGPT

Use SalesFlow when the user asks in Chinese or English for customer research, conversation recap,
follow-up drafting, daily sales briefing, meeting prep, competitive response, pipeline review, or
quote readiness.

Always apply these rules:

1. Detect the workflow using `core/trigger-map.yaml`.
2. Separate source evidence, stable customer facts, one-off activity, reusable sales knowledge,
   personal learning, lightweight tracker updates, and quotation handoff.
3. State evidence levels for important claims.
4. Stop if customer identity or raw source evidence is missing.
5. Produce a `write_plan` before any durable write.
6. Ask for confirmation before writing.
7. Read back after writing and summarize the result.
8. Customer-facing drafts are plain text and do not include signatures by default.

Use `adapters/chatgpt/actions.openapi.yaml` as the optional Actions contract when tools are available.

