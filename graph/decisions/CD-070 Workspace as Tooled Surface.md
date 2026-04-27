---
id: CD-070
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-070.md
generated: 2026-04-27T00:41:01Z
---

# CD-070: Workspace as Tooled Surface

**Status:** Active
**Source:** `kos/decisions/CD-070.md`

## Relationships

**amends:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Class A artifacts pragmatically introduced in CD-067 (Events/meridian-session, Events/kc-findings, Events/design-feedback) now formally governed by CD-070 — Events/ subdirs retire as primary homes in favor of ops/<type>/ canonical + workspace/_meridian-ops/<type>/ mirror (ms-20260421-0611)), [[CD-061 Notebook Hub-Served Knowledge Surface|Notebook Hub-Served Knowledge Surface]] (Workspace ownership framework (CD-070) subsumes CD-061 Notebook Hub-Served Knowledge Surface scope — notebook content classified under the Class A/B/C deletion-test taxonomy; knowledge surface governance flows through CD-070 Pillars 1-3 (ms-20260421-0611)), [[CD-068 True Tool Surface for Meridian|True Tool Surface for Meridian]] (CD-070 Pillar 3 schema enforcement integrates with CD-068 True Tool Surface — typed writes routed via meridian_ops_* MCP tool family share Pydantic schema discipline with Capability Registry (ms-20260421-0611))
**created:** [[TOOL-MIGRATE-SESSIONS-TO-OPS|TOOL-MIGRATE-SESSIONS-TO-OPS]] (CD-070 Phase 1 migration tool (landed cc-20260420-0609) (ms-20260421-0611))
**governed-by:** [[CP-012|CP-012]] (Machine-First Design governs Workspace ownership schema — CD-070 Pillar 3 schema enforcement is machine-first reasoning embedded (AUDIT-2026-04-24-001 fix, ms-20260425-0554))
**referenced-by:** [[CP-010|CP-010]] (Capture Routing surface #1 (Class A canonicals) and surface #2 (Class B Workspace) per "Relationship to CD-070" body section (AUDIT-2026-04-24-001 fix, ms-20260425-0554))
