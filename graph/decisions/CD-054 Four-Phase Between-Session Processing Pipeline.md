---
id: CD-054
type: decision
tags: [decision]
status: Active
source: .kos/decisions/CD-054.md
generated: 2026-04-17T23:30:55Z
---

# CD-054: Four-Phase Between-Session Processing Pipeline

**Status:** Active
**Source:** `.kos/decisions/CD-054.md`

## Relationships

**extends:** [[CD-047 LaunchAgent as Execution Layer|LaunchAgent as Execution Layer]] (Four-phase pipeline extends LaunchAgent execution layer), [[CD-053 Audit Finding Severity Scoring and Recurrence Tracking|Audit Finding Severity Scoring and Recurrence Tracking]] (Pipeline Analyze/Synthesize phases extend severity scoring), [[CD-011 Corpus Consistency Auditing|Corpus Consistency Auditing]] (Pipeline includes lightweight audit as Phase 2 capability)
**governs:** [[TASK-KCP KC Pipeline|KC Pipeline]] (KC pipeline becomes named Phase 2 capability)
**extended-by:** [[CD-055 Semantic Surfaces as Layered Reasoning Infrastructure|Semantic Surfaces as Layered Reasoning Infrastructure]] (Hub surface need precipitated by four-phase pipeline Synthesize phase), [[CD-056 Sleep Mode — System-Driven Session Posture|Sleep Mode — System-Driven Session Posture]] (Sleep mode executes the four-phase pipeline), [[CD-059 Audit Remediation as Sleep Mode Pipeline Phase|Audit Remediation as Sleep Mode Pipeline Phase]] (Adds Remediate phase to four-phase pipeline), [[CD-060 Hub as Cross-Domain Router — Retire Feed Files|Hub as Cross-Domain Router — Retire Feed Files]] (Phase 3 Synthesize gains cross-domain routing responsibility), [[CD-064 Goal-Focused Evaluation Framework|Goal-Focused Evaluation Framework]] (Adds Phase 2d goal-focused evaluation to pipeline), [[CD-066 Autonomous Execution Architecture|Autonomous Execution Architecture]] (Autonomous execution architecture provides execution infrastructure for the four-phase pipeline)
**referenced-by:** [[MO-254 Hub four-phase between-session processing pipeline — IngestAnalyzeSynthesiz...|Hub four-phase between-session processing pipeline — Ingest/Analyze/Synthesiz...]] (Referenced in MO-254), [[MO-255 Obsidian graph view as generated view layer — read-only wiki-linked output fr...|Obsidian graph view as generated view layer — read-only wiki-linked output fr...]] (Referenced in MO-255), [[MO-256 Scheduled task vs|Scheduled task vs]] (Referenced in MO-256), [[MO-262 Sleep Mode provenance — DiscoverWildScience article seeded CD-056057 concept...|Sleep Mode provenance — DiscoverWildScience article seeded CD-056/057 concept...]] (Referenced in MO-262), [[MO-265 Behavioral Activation gap — deploying decisions ≠ activating behaviors|Behavioral Activation gap — deploying decisions ≠ activating behaviors]] (Referenced in MO-265), [[MO-295 Hub Sleep Mode pipeline commit scope — pipeline committed only hubnotificati...|Hub Sleep Mode pipeline commit scope — pipeline committed only hub/notificati...]] (Referenced in MO-295), [[MO-296 Generated-artifact commit lag hides architectural visibility|Generated-artifact commit lag hides architectural visibility]] (Referenced in MO-296)
