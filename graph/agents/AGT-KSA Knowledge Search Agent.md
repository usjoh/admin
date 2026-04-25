---
id: AGT-KSA
type: agent
tags: [agent]
status: Core-ready
source: kos/agents/ksa-1.md
generated: 2026-04-25T12:55:26Z
---

# AGT-KSA: Knowledge Search Agent

**Status:** Core-ready
**Source:** `kos/agents/ksa-1.md`

## Relationships

**depends-on:** [[CD-032 Meridian-owned search via mcp-local-rag|Meridian-owned search via mcp-local-rag]] (mcp-local-rag search index)
**implements:** [[PROT-KSA KSA Protocol|KSA Protocol]] (Cross-session search)
**created-by:** [[CD-031 CSA-as-broker for KSA|CSA-as-broker for KSA]] (CSA-as-broker pattern)
**governed-by:** [[CD-048 Unified Execution Pattern Skills and Agents as Deployment Modes|Unified Execution Pattern: Skills and Agents as Deployment Modes]] (Skills and agents as deployment modes of same execution pattern), [[CD-036 Thin orchestrator + formal agents|Thin orchestrator + formal agents]] (Thin orchestrator architecture), [[CD-032 Meridian-owned search via mcp-local-rag|Meridian-owned search via mcp-local-rag]] (mcp-local-rag search architecture governs KSA), [[CP-004|CP-004]] (Agent File Ownership governs KSA working-memory write scope and search-result envelope ownership (ms-20260421-0611))
