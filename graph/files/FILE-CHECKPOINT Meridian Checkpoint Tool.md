---
id: FILE-CHECKPOINT
type: file
tags: [file]
status: Active
source: kos/tools/meridian-checkpoint.sh
generated: 2026-04-20T04:34:13Z
---

# FILE-CHECKPOINT: Meridian Checkpoint Tool

**Status:** Active
**Source:** `kos/tools/meridian-checkpoint.sh`

## Relationships

**implements:** [[CONV-ROW2 Row 2 Checkpoint Pattern|Row 2 Checkpoint Pattern]] (Canonical callable checkpoint mechanism (Row 2 #1, cc-20260417-0609). Target repointed to registered CONV-ROW2 entity cc-20260419-0708 per CD-009 hybrid policy amendment.)
**inv-uses:** [[operational-model-session-close.md|operational-model/session-close.md]] (Calls meridian-checkpoint.sh for git checkpoint step), [[operational-model-github-operations.md|operational-model/github-operations.md]] (Calls meridian-checkpoint.sh for git checkpoint step)
**referenced-by:** [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (Row 2 shell-script pattern is the motivating comparison; CD-068 may supersede or refine it)
