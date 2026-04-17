---
id: TASK-KCP
type: task
tags: [task]
status: Core-ready
source: .kos/tasks/kc-pipeline.md
generated: 2026-04-17T09:57:50Z
---

# TASK-KCP: KC Pipeline

**Status:** Core-ready
**Source:** `.kos/tasks/kc-pipeline.md`

## Relationships

**depends-on:** [[AGT-KC Knowledge Capture Agent|Knowledge Capture Agent]] (Pipeline spawns KC agent), [[PROT-KC KC Protocol|KC Protocol]] (Pipeline follows KC protocol)
**created-by:** [[CD-007 Autonomous KC (Smart KC)|Autonomous KC (Smart KC)]] (KC Pipeline task)
**depended-on-by:** [[CD-011 Corpus Consistency Auditing|Corpus Consistency Auditing]] (Lightweight audit runs as pipeline Step 5e)
**governed-by:** [[CD-040 Corpus sources with path-pattern validation|Corpus sources with path-pattern validation]] (Corpus source validation), [[CD-054 Four-Phase Between-Session Processing Pipeline|Four-Phase Between-Session Processing Pipeline]] (KC pipeline becomes named Phase 2 capability)
