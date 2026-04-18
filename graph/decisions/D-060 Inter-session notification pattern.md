---
id: D-060
type: decision
tags: [decision]
status: Active
source: .kos/decisions/D-060.md
generated: 2026-04-18T12:13:27Z
---

# D-060: Inter-session notification pattern

**Status:** Active
**Source:** `.kos/decisions/D-060.md`

## Relationships

**amends:** [[D-055 TIA as transcript ingestion validator with executor-ready design|TIA as transcript ingestion validator with executor-ready design]] (Status field in D-055)
**extends:** [[CD-029 Hook-based STA-to-CSA injection|Hook-based STA-to-CSA injection]] (Notification pattern extends hook injection)
**retires:** [[AGT-TIA Transcript Ingestion Agent (retired)|Transcript Ingestion Agent (retired)]] (Hub notification pattern retires TIA session-start role)
**amended-by:** [[CD-067 Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files|Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files]] (Active session detection retired; liveness via manifest directory + Workspace status)
**depended-on-by:** [[CC-005 Corpus Maintenance Agent|Corpus Maintenance Agent]] (Hub notification pattern replaced TIA)
**extended-by:** [[CD-060 Hub as Cross-Domain Router — Retire Feed Files|Hub as Cross-Domain Router — Retire Feed Files]] (Hub absorbs cross-domain routing function)
**referenced-by:** [[MO-164 Scheduled tasks self-block via active-session marker|Scheduled tasks self-block via active-session marker]] (Referenced in MO-164), [[MO-165 STA summary status as active-session proxy is fragile|STA summary status as active-session proxy is fragile]] (Referenced in MO-165), [[MO-166 Hub subscriber file schema (required sections, field names, RAG index referen...|Hub subscriber file schema (required sections, field names, RAG index referen...]] (Referenced in MO-166), [[MO-168 Scheduled task platform limitations block autonomous Hub operation|Scheduled task platform limitations block autonomous Hub operation]] (Referenced in MO-168), [[MO-186 Hub notification file has no autonomous checkpointtruncation mechanism — con...|Hub notification file has no autonomous checkpoint/truncation mechanism — con...]] (Referenced in MO-186), [[MO-188 Hub corpus-maintenance can extract transcripts (Python, no MCP) but cannot in...|Hub corpus-maintenance can extract transcripts (Python, no MCP) but cannot in...]] (Referenced in MO-188), [[MO-254 Hub four-phase between-session processing pipeline — IngestAnalyzeSynthesiz...|Hub four-phase between-session processing pipeline — Ingest/Analyze/Synthesiz...]] (Referenced in MO-254)
