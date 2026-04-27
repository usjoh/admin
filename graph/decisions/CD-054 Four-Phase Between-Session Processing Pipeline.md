---
id: CD-054
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-054.md
generated: 2026-04-27T21:50:26Z
---

# CD-054: Four-Phase Between-Session Processing Pipeline

**Status:** Active
**Source:** `kos/decisions/CD-054.md`

## Relationships

**depends-on:** [[TOOL-EXTRACT-TRANSCRIPTS|TOOL-EXTRACT-TRANSCRIPTS]] (Four-Phase between-session pipeline (Phase 1a ingest) depends on transcript extraction tool (ms-20260421-0611))
**extends:** [[CD-047 LaunchAgent as Execution Layer|LaunchAgent as Execution Layer]] (Four-phase pipeline extends LaunchAgent execution layer), [[CD-053 Audit Finding Severity Scoring and Recurrence Tracking|Audit Finding Severity Scoring and Recurrence Tracking]] (Pipeline Analyze/Synthesize phases extend severity scoring), [[CD-011 Corpus Consistency Auditing|Corpus Consistency Auditing]] (Pipeline includes lightweight audit as Phase 2 capability)
**governs:** [[TASK-KCP KC Pipeline|KC Pipeline]] (KC pipeline becomes named Phase 2 capability)
**amended-by:** [[CD-071 Corpus Dispatcher|Corpus Dispatcher]] (Phase 1b corpus validation migrates from per-domain server name discovery to domain-argument pattern (ms-20260421-0611))
**extended-by:** [[CD-055 Semantic Surfaces as Layered Reasoning Infrastructure|Semantic Surfaces as Layered Reasoning Infrastructure]] (Hub surface need precipitated by four-phase pipeline Synthesize phase), [[CD-056 Sleep Mode — System-Driven Session Posture|Sleep Mode — System-Driven Session Posture]] (Sleep mode executes the four-phase pipeline), [[CD-059 Audit Remediation as Sleep Mode Pipeline Phase|Audit Remediation as Sleep Mode Pipeline Phase]] (Adds Remediate phase to four-phase pipeline), [[CD-060 Hub as Cross-Domain Router — Retire Feed Files|Hub as Cross-Domain Router — Retire Feed Files]] (Phase 3 Synthesize gains cross-domain routing responsibility), [[CD-064 Goal-Focused Evaluation Framework|Goal-Focused Evaluation Framework]] (Adds Phase 2d goal-focused evaluation to pipeline), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Autonomous execution architecture provides execution infrastructure for the four-phase pipeline)
