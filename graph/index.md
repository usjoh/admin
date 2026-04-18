---
type: index
generated: 2026-04-18T18:35:53Z
---

# Meridian Graph

Auto-generated from `core-relationships.md`, `decision-log/relationships.md`, and `current-state/observations/relationships.md`. Do not edit.

**Entities:** 113 | **Relationships:** 167

## Decisions (71)

- CD-001 — Namespaced decision numbering `Active (amended by CD-041)`
- CD-002 — Core/Domain separation `Active`
- CD-003 — Active session false-close fix `Active`
- CD-004 — Meridian/CC session decoupling `Active`
- CD-005 — Mode transparency `Open`
- CD-006 — System observability `Open`
- CD-007 — Autonomous KC (Smart KC) `Active`
- CD-008 — Developer Write Agent `Active`
- CD-009 — Core Entity-Relationship Graph `Active`
- CD-010 — Concern-Based Self-Tracking `Active`
- CD-011 — Corpus Consistency Auditing `Active`
- CD-012 — Adopt Meridian KOS standard `Active`
- CD-013 — Prototype kernel pattern `Active`
- CD-014 — Core behavioral principles `Active`
- CD-015 — Auto-memory is platform feature `Active`
- CD-016 — Simpler interventions before Agent SDK `Active`
- CD-017 — Core vision/identity as infrastructure `Active`
- CD-018 — Capability Completeness principle `Active`
- CD-019 — Core self-description via system-map `Active`
- CD-020 — Decision log status lifecycle `Active`
- CD-021 — Core-vision.md self-referential principle `Active`
- CD-022 — Safety check in session close `Active`
- CD-023 — STA as first Core agent service `Active`
- CD-024 — .meridian/ as local-first directory `Active`
- CD-025 — Subdomain structural requirements `Active`
- CD-026 — LWA for all domain writes `Active`
- CD-027 — Pin MCP server state to absolute paths `Active`
- CD-028 — STA pivot to session awareness `Active`
- CD-029 — Hook-based STA-to-CSA injection `Active`
- CD-030 — Transcript archival during session close `Active`
- CD-031 — CSA-as-broker for KSA `Active`
- CD-032 — Meridian-owned search via mcp-local-rag `Active`
- CD-033 — Transcript extraction for search `Active`
- CD-034 — Core Sync full deployment surface `Active`
- CD-035 — Adopt shared credential convention `Active`
- CD-036 — Thin orchestrator + formal agents `Active`
- CD-037 — Agent Teams as structural enforcement `Active`
- CD-038 — Git as checkpoint, not coordination `Active`
- CD-039 — Decision log split into index + entries `Active`
- CD-040 — Corpus sources with path-pattern validation `Active`
- CD-041 — Core Decision Boundary Enforcement `Active`
- CD-042 — CSA Motivation: Self-knowledge serves current task `Superseded by CD-044`
- CD-043 — Dual-Core Architecture `Active`
- CD-044 — CSA Behavioral Design: Align With the Greedy Agent `Active`
- CD-045 — Two-Tier KC Model `Active`
- CD-046 — KC Two-Bucket Output Model `Active`
- CD-047 — LaunchAgent as Execution Layer `Active`
- CD-048 — Unified Execution Pattern: Skills and Agents as Deployment Modes `Active`
- CD-049 — Orchestration Policy as Named Core Concept `Active`
- CD-050 — Five-Component Ambient Architecture `Active`
- CD-051 — Agent Definition Standard `Active`
- CD-052 — Signal File Redesign — Nudge Not Payload `Active`
- CD-053 — Audit Finding Severity Scoring and Recurrence Tracking `Active`
- CD-054 — Four-Phase Between-Session Processing Pipeline `Active`
- CD-055 — Semantic Surfaces as Layered Reasoning Infrastructure `Active`
- CD-056 — Sleep Mode — System-Driven Session Posture `Active`
- CD-057 — Working-Memory Lifecycle Management `Active`
- CD-058 — Domain Relationship Infrastructure `Active`
- CD-059 — Audit Remediation as Sleep Mode Pipeline Phase `Active`
- CD-060 — Hub as Cross-Domain Router — Retire Feed Files `Active`
- CD-061 — Notebook Hub-Served Knowledge Surface `Active`
- CD-062 — Sleep Mode as Execution Model — Retire LaunchAgents `Active`
- CD-063 — Domain Sleep Mode Inherits Hub Pipeline `Active`
- CD-064 — Goal-Focused Evaluation Framework `Active`
- CD-065 — I/O Interface Architecture `Active`
- CD-066 — Autonomous Execution Architecture `Active`
- CD-067 — Workspace as Session Surface; Retire STA, Liveness Hooks, Signal Files `Active`
- CD-068 — True Tool Surface for Meridian `Draft`
- CD-069 — Core Graduation to Meridian `Active`
- D-058 — Separate Core from domain decisions `Active`
- D-060 — Inter-session notification pattern `Active`

## Agents (6)

- AGT-DWA — Developer Write Agent `Core-ready`
- AGT-KC — Knowledge Capture Agent `Core-ready`
- AGT-KSA — Knowledge Search Agent `Core-ready`
- AGT-LWA — Layer Writer Agent `Core-ready`
- AGT-STA — Session Transcript Agent `Retired (CD-067)`
- AGT-TIA — Transcript Ingestion Agent (retired) `Retired (D-060)`

## Protocols (5)

- PROT-KC — KC Protocol `Core-ready`
- PROT-KSA — KSA Protocol `Core-ready`
- PROT-LIFECYCLE — Session Lifecycle `Validated`
- PROT-LWA — LWA Protocol `Core-ready`
- PROT-STA — STA Protocol `Retired (CD-067)`

## Tasks (1)

- TASK-KCP — KC Pipeline `Core-ready`

## Files (18)

- FILE-AUDIT — Core Audit Protocol `Active`
- FILE-CHANGELOG — Core Changelog `Active`
- FILE-CHECKPOINT — Meridian Checkpoint Tool `Active`
- FILE-CLAUDE — CLAUDE.md Entry Point `Core-ready`
- FILE-CODEMAP — Code Map `Active`
- FILE-COMPACTLDB — LanceDB Compaction Tool `Active`
- FILE-CURSTATE — Core Current State `Core-ready`
- FILE-DECISIONS — Core Decisions `Core-ready`
- FILE-DETECTUNCOMMITTED — Detect Uncommitted Work Tool `Active`
- FILE-EXTRACTREL — Domain Relationship Extractor `Active`
- FILE-GRAPHGEN — Graph Generator `Active`
- FILE-INCRCHECK — Incremental Corpus Check Tool `Active`
- FILE-PRINCIPLES — Core Principles `Core-ready`
- FILE-REL — Core Relationships `Active`
- FILE-SETTINGS — Core Settings Template `Core-ready`
- FILE-SYSMAP — Core System Map `Validated`
- FILE-VISION — Core Vision `Validated`
- FILE-VISIONNARR — Core Vision Narrative `Validated`

## Conventions (7)

- CONV-CAPCOMP — Capability Completeness `Active`
- CONV-CONSULT — Consult Before Solving `Active`
- CONV-DLFMT — Decision log format `Active`
- CONV-DLSTAT — Decision status lifecycle `Active`
- CONV-KCSUMM — KC Summary as primary session artifact `Active`
- CONV-SESSLOG — Session logs as cold storage `Active`
- CROSS-DOMAIN-FEED — Cross-Domain Feed File Mechanism (retired) `Superseded`

## Concerns (5)

- CC-001 — Agent reasoning depth `Active`
- CC-002 — Simpler interventions (CD-016) `Active`
- CC-003 — Multi-agent architecture `Active`
- CC-004 — File contention `Resolved`
- CC-005 — Corpus Maintenance Agent `Active`
