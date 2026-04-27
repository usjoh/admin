---
id: CD-011
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-011.md
generated: 2026-04-27T21:50:26Z
---

# CD-011: Corpus Consistency Auditing

**Status:** Active
**Source:** `kos/decisions/CD-011.md`

## Relationships

**created:** [[FILE-AUDIT Core Audit Protocol|Core Audit Protocol]] (Core audit protocol)
**depends-on:** [[TASK-KCP KC Pipeline|KC Pipeline]] (Lightweight audit runs as pipeline Step 5e)
**extends:** [[CD-009 Core Entity-Relationship Graph|Core Entity-Relationship Graph]] (Uses relationship graph for integrity checks), [[CD-010 Concern-Based Self-Tracking|Concern-Based Self-Tracking]] (Uses concern tracking for staleness checks)
**extended-by:** [[CD-053 Audit Finding Severity Scoring and Recurrence Tracking|Audit Finding Severity Scoring and Recurrence Tracking]] (Severity scoring extends corpus consistency auditing), [[CD-054 Four-Phase Between-Session Processing Pipeline|Four-Phase Between-Session Processing Pipeline]] (Pipeline includes lightweight audit as Phase 2 capability), [[CD-006 System observability|System observability]] (System observability addressed by audit protocol), [[CD-072 Layer-Aware Graph Health Analysis|Layer-Aware Graph Health Analysis]] (Topology-based findings extend CD-011 core audit protocol — adds structural-layer tier alongside existing Tier 1/2/3 audit checks (ms-20260421-0611))
