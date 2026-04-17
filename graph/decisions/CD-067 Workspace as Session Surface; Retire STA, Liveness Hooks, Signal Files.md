---
id: CD-067
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-067.md
generated: 2026-04-17T17:11:01Z
---

# CD-067: Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files

**Status:** Active
**Source:** `.kos/decisions/CD-067.md`

## Relationships

**amends:** [[D-060 Inter-session notification pattern|Inter-session notification pattern]] (Active session detection retired; liveness via manifest directory + Workspace status), [[CD-003 Active session false-close fix|Active session false-close fix]] (Stop hook purpose redefined from liveness to continuous git checkpointing), [[CD-004 MeridianCC session decoupling|Meridian/CC session decoupling]] (Checkpoint operation simplified; STA lifecycle retired), [[CD-007 Autonomous KC (Smart KC)|Autonomous KC (Smart KC)]] (STA lifecycle retired; KC findings routed to Workspace)
**extends:** [[CD-050 Five-Component Ambient Architecture|Five-Component Ambient Architecture]] (Workspace session notes and KC finding notes leverage working-memory surface model), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Summary backfill Routine targets Cloud Routines tier for execution), [[CD-038 Git as checkpoint, not coordination|Git as checkpoint, not coordination]] (Per-turn commit checkpointing extends git-as-checkpoint model to continuous cadence), [[CD-052 Signal File Redesign — Nudge Not Payload|Signal File Redesign — Nudge Not Payload]] (Signal file retired entirely; working memory + ambient query replace coordination need)
**resolves:** [[MO-294 Stop hook trigger frequency — refinement question for CD-003|Stop hook trigger frequency — refinement question for CD-003]] (Resolution recorded in MO-294)
**retires:** [[AGT-STA Session Transcript Agent|Session Transcript Agent]] (STA agent retired; orientation roles absorbed by CSA), [[PROT-STA STA Protocol|STA Protocol]] (STA protocol deprecated; replaced by Workspace-first session-surface protocol)
**referenced-by:** [[MO-294 Stop hook trigger frequency — refinement question for CD-003|Stop hook trigger frequency — refinement question for CD-003]] (Referenced in MO-294), [[MO-295 Hub Sleep Mode pipeline commit scope — pipeline committed only hubnotificati...|Hub Sleep Mode pipeline commit scope — pipeline committed only hub/notificati...]] (Referenced in MO-295), [[MO-296 Generated-artifact commit lag hides architectural visibility|Generated-artifact commit lag hides architectural visibility]] (Referenced in MO-296)
