---
id: CD-067
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-067.md
generated: 2026-04-27T01:32:14Z
---

# CD-067: Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files

**Status:** Active
**Source:** `kos/decisions/CD-067.md`

## Relationships

**amends:** [[D-060 Inter-session notification pattern|Inter-session notification pattern]] (Active session detection retired; liveness via manifest directory + Workspace status), [[CD-003 Active session false-close fix|Active session false-close fix]] (Stop hook purpose redefined from liveness to continuous git checkpointing), [[CD-004 MeridianCC session decoupling|Meridian/CC session decoupling]] (Checkpoint operation simplified; STA lifecycle retired), [[CD-007 Autonomous KC (Smart KC)|Autonomous KC (Smart KC)]] (STA lifecycle retired; KC findings routed to Workspace)
**extends:** [[CD-050 Five-Component Ambient Architecture|Five-Component Ambient Architecture]] (Workspace session notes and KC finding notes leverage working-memory surface model), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Summary backfill Routine targets Cloud Routines tier for execution), [[CD-038 Git as checkpoint, not coordination|Git as checkpoint, not coordination]] (Per-turn commit checkpointing extends git-as-checkpoint model to continuous cadence), [[CD-052 Signal File Redesign — Nudge Not Payload|Signal File Redesign — Nudge Not Payload]] (Signal file retired entirely; working memory + ambient query replace coordination need)
**implemented-by:** [[TOOL-DETECT-UNCOMMITTED-WORK|TOOL-DETECT-UNCOMMITTED-WORK]] (Phase 3 — session-start uncommitted-work detection)
**implements:** [[TOOL-HOOK-PRE-COMPACT|TOOL-HOOK-PRE-COMPACT]] (Session surface (CD-067) instruments pre-compact boundary via this hook (ms-20260421-0611)), [[TOOL-HOOK-SESSION-END|TOOL-HOOK-SESSION-END]] (Session surface (CD-067) instruments session-end marker via this hook (ms-20260421-0611))
**retires:** [[AGT-STA Session Transcript Agent|Session Transcript Agent]] (STA agent retired; orientation roles absorbed by CSA), [[PROT-STA STA Protocol|STA Protocol]] (STA protocol deprecated; replaced by Workspace-first session-surface protocol)
**amended-by:** [[CD-069 Core Graduation to Meridian|Core Graduation to Meridian]] (Replaces Phase 8 (copy-based Core Sync propagation) with Meridian-reference model; all other CD-067 phases intact), [[CD-070 Workspace as Tooled Surface|Workspace as Tooled Surface]] (Class A artifacts pragmatically introduced in CD-067 (Events/meridian-session, Events/kc-findings, Events/design-feedback) now formally governed by CD-070 — Events/ subdirs retire as primary homes in favor of ops/<type>/ canonical + workspace/_meridian-ops/<type>/ mirror (ms-20260421-0611))
