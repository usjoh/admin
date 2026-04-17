---
id: CD-038
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-038.md
generated: 2026-04-17T09:57:50Z
---

# CD-038: Git as checkpoint, not coordination

**Status:** Active
**Source:** `.kos/decisions/CD-038.md`

## Relationships

**governs:** [[PROT-LIFECYCLE Session Lifecycle|Session Lifecycle]] (Git-as-checkpoint model governs session lifecycle)
**extended-by:** [[CD-004 MeridianCC session decoupling|Meridian/CC session decoupling]] (Session identity decoupled from CC), [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Per-turn commit checkpointing extends git-as-checkpoint model to continuous cadence)
**inv-governed-by:** [[CONV-SESSLOG Session logs as cold storage|Session logs as cold storage]] (Session logs as cold storage governed by git-as-checkpoint)
