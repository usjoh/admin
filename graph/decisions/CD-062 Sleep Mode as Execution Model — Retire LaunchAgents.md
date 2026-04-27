---
id: CD-062
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-062.md
generated: 2026-04-27T12:04:56Z
---

# CD-062: Sleep Mode as Execution Model — Retire LaunchAgents

**Status:** Active
**Source:** `kos/decisions/CD-062.md`

## Relationships

**governs:** [[[concept]-Sleep-Mode-as-execution-model|[concept] Sleep Mode as execution model]] (LaunchAgents retired; Sleep Mode is single execution context (concept target per CD-009 hybrid policy, amended 2026-04-19))
**amended-by:** [[CD-063 Domain Sleep Mode Inherits Hub Pipeline|Domain Sleep Mode Inherits Hub Pipeline]] (Domain Sleep Mode inherits Hub pipeline (adds domain execution path)), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Partially reverses scheduled task retirement — LaunchD returns as scheduling layer)
**implemented-by:** [[TOOL-COMPACT-LANCEDB|TOOL-COMPACT-LANCEDB]] (LanceDB compaction tool implements Sleep Mode pipeline post-step), [[TOOL-INCREMENTAL-CORPUS-CHECK|TOOL-INCREMENTAL-CORPUS-CHECK]] (Incremental corpus check implements CD-062 validation pattern)
