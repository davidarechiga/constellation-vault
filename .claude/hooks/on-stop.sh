#!/bin/bash
# on-stop.sh — AI-summarized session log writer
# Runs on Claude Code Stop event. Appends a summarized entry to the rolling Session Log.

VAULT="/Users/davidarechiga/Constellation/Constellation"
GIT_ROOT="/Users/davidarechiga/Constellation"
SESSION_LOG="$VAULT/C - Signal Relay/Session Log.md"
DATETIME=$(date +"%Y-%m-%d %H:%M")

# Find changed vault .md files via git status
CHANGED_FILES=$(cd "$GIT_ROOT" && git status --short -- "Constellation/*.md" 2>/dev/null \
  | grep -v "_index.md" \
  | grep -v "Daily/" \
  | grep -v "Weekly/" \
  | awk '{print $2}' \
  | xargs -I{} basename {} .md \
  | head -10 \
  | tr '\n' ',' \
  | sed 's/,$//')

# Create Session Log if it doesn't exist
if [ ! -f "$SESSION_LOG" ]; then
  cat > "$SESSION_LOG" << 'EOF'
# Session Log

Chronological log of Claude Code sessions in this vault.

EOF
fi

# If no vault files changed, write a minimal no-op entry and exit
if [ -z "$CHANGED_FILES" ]; then
  cat >> "$SESSION_LOG" << EOF

### $DATETIME
*(no vault files modified)*

EOF
  exit 0
fi

# Build wikilinks from changed file names
WIKILINKS=$(echo "$CHANGED_FILES" | tr ',' '\n' | sed 's/^ //' | sed 's/^/[[/' | sed 's/$/]]/' | tr '\n' ', ' | sed 's/, $//')

# Get the git diff for changed files (trimmed to avoid huge diffs)
DIFF=$(cd "$GIT_ROOT" && git diff HEAD -- "Constellation/*.md" 2>/dev/null | head -150)

# Call claude -p for a real summary (15s timeout, fallback to file list on failure)
if [ -n "$DIFF" ]; then
  SUMMARY=$(timeout 15 claude -p "You are summarizing a Claude Code session in an Obsidian vault. Based on the git diff below, write ONE sentence (max 20 words) describing what was worked on. Be specific — name the topic or files. Output ONLY the sentence, no preamble.

$DIFF" 2>/dev/null)
fi

# Fallback if AI call failed or returned empty
if [ -z "$SUMMARY" ]; then
  SUMMARY="Modified vault files: $CHANGED_FILES"
fi

cat >> "$SESSION_LOG" << EOF

### $DATETIME
**Summary:** $SUMMARY
**Files:** $WIKILINKS

EOF

exit 0
