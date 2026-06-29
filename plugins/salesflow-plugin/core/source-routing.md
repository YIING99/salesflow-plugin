# Source Routing

SalesFlow separates evidence, sales memory, personal learning, lightweight tracking, quotation work,
and readable archives. It is an orchestration layer, not a replacement system.

## Routing Rules

- Raw source evidence stays in its source location: email, chat export, meeting transcript, local
  database, uploaded file, or archive folder.
- Stable customer facts and full follow-up records go to the sales knowledge base.
- One-off customer interactions are saved as activity records, not merged into the stable profile.
- Reusable product knowledge, competitive notes, and objection handling go to the sales knowledge base.
- Personal methods, preferences, and cross-project lessons go to the personal knowledge base.
- Lightweight stage, risk, reminder, next action, owner, and dashboard fields go to the tracker.
- Quotation-specific checks and workbook generation stay in the quotation workflow.
- Readable reports or customer folders go to the local archive only when the user asks for that output.

## Default Persistence Targets

| Material | Target |
| --- | --- |
| Customer identity and stable profile | sales knowledge base |
| Email, call, meeting, chat event | sales knowledge base activity |
| Stage, risk, next reminder | lightweight tracker |
| Product fact, objection, competitor response | sales knowledge base |
| Personal process lesson | personal knowledge base |
| Quote readiness and missing inputs | quotation workflow |
| Full raw transcript or chat stream | source evidence layer |
| Customer-readable report copy | local archive |

## Stop Conditions

Stop and ask for missing evidence when customer identity is ambiguous, raw source material is absent,
or the user asks for a customer-facing draft that could mix facts from different customers.

