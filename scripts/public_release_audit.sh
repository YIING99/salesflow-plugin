#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 "$ROOT/plugins/salesflow-plugin/scripts/validate_salesflow.py"
python3 -m json.tool "$ROOT/.agents/plugins/marketplace.json" >/dev/null
python3 -m json.tool "$ROOT/plugins/salesflow-plugin/.codex-plugin/plugin.json" >/dev/null
python3 -m json.tool "$ROOT/plugins/salesflow-plugin/core/output-schemas/write_plan.json" >/dev/null

if find "$ROOT" -name ".DS_Store" -o -name "__pycache__" | grep -q .; then
  echo "Private or generated file found."
  exit 1
fi

if find "$ROOT" \
  \( -name ".env" -o -name ".env.*" -o -name "auth.json" -o -name "credentials.json" -o -name "secrets.json" -o -name "*.pem" -o -name "*.key" \) \
  | grep -q .; then
  echo "Sensitive filename found."
  exit 1
fi

LOCAL_HOME_PATTERN="/""Users/"
GITHUB_TOKEN_PATTERN="gh""o_[A-Za-z0-9_]+"
OPENAI_KEY_PATTERN="sk-""[A-Za-z0-9_-]{20,}"
AWS_KEY_PATTERN="AKIA""[0-9A-Z]{16}"
PRIVATE_KEY_PATTERN="BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY"
SENSITIVE_VALUE_PATTERN="${LOCAL_HOME_PATTERN}|${GITHUB_TOKEN_PATTERN}|${OPENAI_KEY_PATTERN}|${AWS_KEY_PATTERN}|${PRIVATE_KEY_PATTERN}"

if rg -n "$SENSITIVE_VALUE_PATTERN" "$ROOT"; then
  echo "Sensitive value pattern found."
  exit 1
fi

if [[ -n "${SALESFLOW_BANNED_TERMS:-}" ]]; then
  IFS="," read -r -a TERMS <<< "$SALESFLOW_BANNED_TERMS"
  for term in "${TERMS[@]}"; do
    trimmed="$(echo "$term" | xargs)"
    if [[ -n "$trimmed" ]] && rg -n -i --fixed-strings "$trimmed" "$ROOT"; then
      echo "Banned private term found: $trimmed"
      exit 1
    fi
  done
fi

if git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git -C "$ROOT" rev-list --all | grep -q .; then
    if git -C "$ROOT" grep -n -I -E "$SENSITIVE_VALUE_PATTERN" $(git -C "$ROOT" rev-list --all) -- . >/tmp/salesflow-history-audit.txt 2>/dev/null; then
      cat /tmp/salesflow-history-audit.txt
      echo "Sensitive value found in git history."
      exit 1
    fi
  fi
else
  echo "Git history audit skipped: repository not initialized yet."
fi

echo "Public release audit passed."
