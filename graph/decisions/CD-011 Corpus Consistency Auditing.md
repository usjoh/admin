---
id: CD-011
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-011.md
generated: 2026-04-17T12:10:36Z
---

# CD-011: Corpus Consistency Auditing

**Status:** Active
**Source:** `.kos/decisions/CD-011.md`

## Relationships

**created:** [[FILE-AUDIT Core Audit Protocol|Core Audit Protocol]] (Core audit protocol)
**depends-on:** [[TASK-KCP KC Pipeline|KC Pipeline]] (Lightweight audit runs as pipeline Step 5e)
**extends:** [[CD-009 Core Entity-Relationship Graph|Core Entity-Relationship Graph]] (Uses relationship graph for integrity checks), [[CD-010 Concern-Based Self-Tracking|Concern-Based Self-Tracking]] (Uses concern tracking for staleness checks)
**extended-by:** [[CD-053 Audit Finding Severity Scoring and Recurrence Tracking|Audit Finding Severity Scoring and Recurrence Tracking]] (Severity scoring extends corpus consistency auditing), [[CD-054 Four-Phase Between-Session Processing Pipeline|Four-Phase Between-Session Processing Pipeline]] (Pipeline includes lightweight audit as Phase 2 capability), [[CD-006 System observability|System observability]] (System observability addressed by audit protocol)
**referenced-by:** [[MO-180 CD-009 Core Entity-Relationship Graph — markdown-table implementation of D-02...|CD-009 Core Entity-Relationship Graph — markdown-table implementation of D-02...]] (Referenced in MO-180), [[MO-181 CD-010 Concern-Based Self-Tracking — 5 initial concerns initialized; D-023 pa...|CD-010 Concern-Based Self-Tracking — 5 initial concerns initialized; D-023 pa...]] (Referenced in MO-181), [[MO-183 Self-referential four-layer loop CD-009010011 maps exactly onto system-map...|Self-referential four-layer loop: CD-009/010/011 maps exactly onto system-map...]] (Referenced in MO-183), [[MO-184 KC Pipeline Audit Extensions pattern (domain.md declarations read at runtime...|KC Pipeline Audit Extensions pattern (domain.md declarations read at runtime...]] (Referenced in MO-184), [[MO-202 'Doesn't know what it doesn't know' gap top-down breaks when agent doesn't k...|'Doesn't know what it doesn't know' gap: top-down breaks when agent doesn't k...]] (Referenced in MO-202), [[MO-252 Audit-driven autonomous propagation and Meridian Sleep mode — patterns propag...|Audit-driven autonomous propagation and Meridian Sleep mode — patterns propag...]] (Referenced in MO-252)
