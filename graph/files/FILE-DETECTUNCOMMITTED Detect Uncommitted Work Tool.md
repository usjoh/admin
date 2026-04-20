---
id: FILE-DETECTUNCOMMITTED
type: file
tags: [file]
status: Active
source: kos/tools/detect-uncommitted-work.sh
generated: 2026-04-20T04:34:13Z
---

# FILE-DETECTUNCOMMITTED: Detect Uncommitted Work Tool

**Status:** Active
**Source:** `kos/tools/detect-uncommitted-work.sh`

## Relationships

**inv-implemented-by:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Phase 3 — session-start uncommitted-work detection)
**inv-uses:** [[kos-hooks-session-start-sta.sh|kos/hooks/session-start-sta.sh]] (Invokes detect-uncommitted-work.sh at session start (CD-067 Phase 3))
