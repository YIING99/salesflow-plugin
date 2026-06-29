# Privacy And Security

SalesFlow is intended to be safe to publish because it contains workflow logic, not private business data.

## Public Release Checklist

Before publishing a fork, verify:

- No `.env`, credentials, API keys, OAuth tokens, cookies, browser storage, or login state.
- No raw customer emails, chat logs, call transcripts, meeting recordings, or CRM exports.
- No private customer names, personal contact details, pricing records, contracts, or order history.
- No local absolute home-directory paths or machine-specific workspace paths.
- No company-specific operating procedures unless deliberately generalized.
- No git history containing deleted secrets or private files.

## Evidence Levels

SalesFlow asks agents to label important claims:

| Level | Source |
| --- | --- |
| L1 | User-confirmed actual behavior or live readback |
| L2 | Local files, structured records, tool output, environment configuration |
| L3 | Official documentation or official public source |
| L4 | Third-party database or multiple external sources |
| L5 | Names, comments, UI labels, seller claims, or model inference |

## Write Safety

Durable writes must follow this order:

```text
write plan -> user confirmation -> write -> readback
```

If readback fails, report the write as unverified.
