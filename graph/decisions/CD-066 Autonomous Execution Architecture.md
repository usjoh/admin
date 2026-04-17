---
id: CD-066
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-066.md
generated: 2026-04-17T09:57:50Z
---

# CD-066: Autonomous Execution Architecture

**Status:** Active
**Source:** `.kos/decisions/CD-066.md`

## Relationships

**amends:** [[CD-062 Sleep Mode as Execution Model — Retire LaunchAgents|Sleep Mode as Execution Model — Retire LaunchAgents]] (Partially reverses scheduled task retirement — LaunchD returns as scheduling layer), [[CD-056 Sleep Mode — System-Driven Session Posture|Sleep Mode — System-Driven Session Posture]] (Sleep Mode no longer sole execution path — Cloud Routines provide autonomous alternative)
**extends:** [[CD-054 Four-Phase Between-Session Processing Pipeline|Four-Phase Between-Session Processing Pipeline]] (Autonomous execution architecture provides execution infrastructure for the four-phase pipeline)
**extended-by:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Summary backfill Routine targets Cloud Routines tier for execution)
