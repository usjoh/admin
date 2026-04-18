---
id: D-060
type: decision
tags: [decision]
status: Active
source: kos/decisions/D-060.md
generated: 2026-04-18T18:35:53Z
---

# D-060: Inter-session notification pattern

**Status:** Active
**Source:** `kos/decisions/D-060.md`

## Relationships

**extends:** [[CD-029 Hook-based STA-to-CSA injection|Hook-based STA-to-CSA injection]] (Notification pattern extends hook injection)
**retires:** [[AGT-TIA Transcript Ingestion Agent (retired)|Transcript Ingestion Agent (retired)]] (Hub notification pattern retires TIA session-start role)
**amended-by:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Active session detection retired; liveness via manifest directory + Workspace status)
**depended-on-by:** [[CC-005 Corpus Maintenance Agent|Corpus Maintenance Agent]] (Hub notification pattern replaced TIA)
**extended-by:** [[CD-060 Hub as Cross-Domain Router — Retire Feed Files|Hub as Cross-Domain Router — Retire Feed Files]] (Hub absorbs cross-domain routing function)
