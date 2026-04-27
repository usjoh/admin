---
id: CD-069
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-069.md
generated: 2026-04-27T12:04:56Z
---

# CD-069: Core Graduation to Meridian

**Status:** Active
**Source:** `kos/decisions/CD-069.md`

## Relationships

**amends:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Replaces Phase 8 (copy-based Core Sync propagation) with Meridian-reference model; all other CD-067 phases intact), [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (Reshapes Q2 (scope) and Q4 (versioning/deployment) under Meridian-resident MCP servers)
**created:** [[FILE-MOCAPTURE Meridian Observation Capture Protocol|Meridian Observation Capture Protocol]] (Meridian Observation Capture promoted to Core protocol (Phase 2.5)), [[FILE-CAPREG Capability Registry|Capability Registry]] (Capability Registry directory. Target repointed to registered FILE-CAPREG entity cc-20260419-0708 per CD-009 hybrid policy amendment.)
**depends-on:** [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (CD-068 formal body drafting unblocked by CD-069 resolution (Q4 dependency))
**extends:** [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Meridian as autonomous-execution substrate aligns with Autonomous Execution Architecture), [[CD-050 Five-Component Ambient Architecture|Five-Component Ambient Architecture]] (Hub-Primary working-memory survives compaction; aligns with Two-Surface memory model), [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (Lifts CD-068 Pydantic schema/Capability Registry pattern to Meridian-wide tool registry (Q13); adopts OB1 n-agentic-harnesses file 03 pattern)
**references:** [[MO-301|MO-301]] (Tool contract discipline — Capability Registry (CD-069 Q13) operationalizes MO-301)
**retires:** [[CD-013 Prototype kernel pattern|Prototype kernel pattern]] (Core-prototyped-in-consulting is a bootstrap artifact, not a principle; consulting becomes a Meridian subdomain), [[MO-270|MO-270]] (Dual-presence pattern (consulting/Meridian overlap) replaced by uniform subdomains/ structure)
**extended-by:** [[CD-071 Corpus Dispatcher|Corpus Dispatcher]] (Corpus Dispatcher β skeleton builds on CD-069 Hub-Primary substrate — Hub-owned MCP server routing per-domain LanceDB queries via `domain` argument (ms-20260421-0611))
**implemented-by:** [[SVC-HUBMCP|SVC-HUBMCP]] (POC vehicle from cc-20260417-1724 validates CD-069 direction)
