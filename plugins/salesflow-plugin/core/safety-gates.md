# Safety Gates

SalesFlow must produce useful sales work without blurring evidence, identity, or persistence layers.

## Evidence Levels

| Level | Source |
| --- | --- |
| L1 | User-confirmed actual behavior or live readback |
| L2 | Local files, structured records, tool output, environment configuration |
| L3 | Official documentation or official public source |
| L4 | Third-party database or multiple external sources |
| L5 | Names, comments, UI labels, seller claims, or model inference |

Key conclusions must state the evidence level. L4/L5 conclusions must include a verification path.

## Pre-Workflow Gates

- Identify the workflow from bilingual triggers or explicit user intent.
- Confirm whether the request needs customer identity, source evidence, or a write plan.
- For customer identity, require at least two hard identifiers when claiming a match.
- If source material is missing, stop and request it instead of reconstructing from memory.
- Separate facts, judgments, estimates, and proposed actions.

## Write Gates

- Never write because a trigger matched.
- Always generate `write_plan` before persistence.
- User confirmation is required before writing to any external or durable system.
- After writing, read back the target object and summarize what was actually saved.
- If readback fails, report the write status as unverified.

## Customer Draft Gates

- Customer-facing drafts must be plain text by default.
- Do not include internal risk language unless the user asks for an internal memo.
- Do not include a signature block by default.
- Do not mix one customer's history, products, pricing, or constraints into another customer's draft.

