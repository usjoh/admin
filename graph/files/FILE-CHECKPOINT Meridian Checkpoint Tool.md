---
id: FILE-CHECKPOINT
type: file
tags: [file]
status: Active
source: .kos/tools/meridian-checkpoint.sh
generated: 2026-04-17T23:30:55Z
---

# FILE-CHECKPOINT: Meridian Checkpoint Tool

**Status:** Active
**Source:** `.kos/tools/meridian-checkpoint.sh`

## Relationships

**implements:** [[Row2-checkpoint-pattern|Row2-checkpoint-pattern]] (Canonical callable checkpoint mechanism (Row 2 #1, cc-20260417-0609) — Row2-checkpoint-pattern not a registered entity; natural-language target used per C-2026-023 pattern)
**inv-uses:** [[operational-model-session-close.md|operational-model/session-close.md]] (Calls meridian-checkpoint.sh for git checkpoint step), [[operational-model-github-operations.md|operational-model/github-operations.md]] (Calls meridian-checkpoint.sh for git checkpoint step)
**referenced-by:** [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (Row 2 shell-script pattern is the motivating comparison; CD-068 may supersede or refine it)
