---
id: CD-068
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-068.md
generated: 2026-04-26T20:47:42Z
---

# CD-068: True Tool Surface for Meridian

**Status:** Active
**Source:** `kos/decisions/CD-068.md`

## Relationships

**extends:** [[CD-048 Unified Execution Pattern Skills and Agents as Deployment Modes|Unified Execution Pattern: Skills and Agents as Deployment Modes]] (True Tool Surface addresses execution pattern at MCP-native layer — extends Unified Execution Pattern), [[CD-050 Five-Component Ambient Architecture|Five-Component Ambient Architecture]] (Tool surface design intersects ambient architecture's surface model)
**references:** [[TOOL-MERIDIAN-CHECKPOINT|TOOL-MERIDIAN-CHECKPOINT]] (Row 2 shell-script pattern is the motivating comparison; CD-068 may supersede or refine it)
**amended-by:** [[CD-069 Core Graduation to Meridian|Core Graduation to Meridian]] (Reshapes Q2 (scope) and Q4 (versioning/deployment) under Meridian-resident MCP servers), [[CD-070 Workspace as Tooled Surface|Workspace as Tooled Surface]] (CD-070 Pillar 3 schema enforcement integrates with CD-068 True Tool Surface — typed writes routed via meridian_ops_* MCP tool family share Pydantic schema discipline with Capability Registry (ms-20260421-0611))
**depended-on-by:** [[CD-069 Core Graduation to Meridian|Core Graduation to Meridian]] (CD-068 formal body drafting unblocked by CD-069 resolution (Q4 dependency))
**extended-by:** [[CD-069 Core Graduation to Meridian|Core Graduation to Meridian]] (Lifts CD-068 Pydantic schema/Capability Registry pattern to Meridian-wide tool registry (Q13); adopts OB1 n-agentic-harnesses file 03 pattern), [[CD-071 Corpus Dispatcher|Corpus Dispatcher]] (CD-071 is the fourth Row 2 application of CD-068 True Tool Surface pattern (after task.*, session.*, meridian_ops_sessions.*) (ms-20260421-0611)), [[CP-011|CP-011]] (True Tool Surface First promotes CD-068 design pattern (MCP wrap + Pydantic + Capability Registry) to a CSA capture-time preference — explicit body reference (AUDIT-2026-04-24-001 fix, ms-20260425-0554))
**governed-by:** [[CP-012|CP-012]] (Machine-First Design governs True Tool Surface — typed contracts are machine-first by construction (AUDIT-2026-04-24-001 fix, ms-20260425-0554))
