---
id: CD-062
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-062.md
generated: 2026-04-17T05:48:41Z
---

# CD-062: Sleep Mode as Execution Model — Retire LaunchAgents

**Status:** Active
**Source:** `.kos/decisions/CD-062.md`

## Relationships

**governs:** [[Sleep-Mode-as-execution-model|Sleep Mode as execution model]] (LaunchAgents retired; Sleep Mode is single execution context)
**amended-by:** [[CD-063 Domain Sleep Mode Inherits Hub Pipeline|Domain Sleep Mode Inherits Hub Pipeline]] (Domain Sleep Mode inherits Hub pipeline (adds domain execution path)), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Partially reverses scheduled task retirement — LaunchD returns as scheduling layer)
**implemented-by:** [[FILE-COMPACTLDB LanceDB Compaction Tool|LanceDB Compaction Tool]] (LanceDB compaction tool implements Sleep Mode pipeline post-step), [[FILE-INCRCHECK Incremental Corpus Check Tool|Incremental Corpus Check Tool]] (Incremental corpus check implements CD-062 validation pattern)
