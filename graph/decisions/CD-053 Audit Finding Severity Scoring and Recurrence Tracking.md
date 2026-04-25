---
id: CD-053
type: decision
tags: [decision]
status: Active
source: kos/decisions/CD-053.md
generated: 2026-04-25T12:55:26Z
---

# CD-053: Audit Finding Severity Scoring and Recurrence Tracking

**Status:** Active
**Source:** `kos/decisions/CD-053.md`

## Relationships

**extends:** [[CD-011 Corpus Consistency Auditing|Corpus Consistency Auditing]] (Severity scoring extends corpus consistency auditing), [[CD-009 Core Entity-Relationship Graph|Core Entity-Relationship Graph]] (Finding tracking uses entity-relationship graph for impact tracing)
**implements:** [[CP-006|CP-006]] (CD-053 Discharge Lifecycle amendment (2026-04-19 cc-20260419-0708) implements Articulation Discharge via discharge-status / discharge-destination / discharge-notes fields (ms-20260421-0611))
**extended-by:** [[CD-054 Four-Phase Between-Session Processing Pipeline|Four-Phase Between-Session Processing Pipeline]] (Pipeline Analyze/Synthesize phases extend severity scoring), [[CD-055 Semantic Surfaces as Layered Reasoning Infrastructure|Semantic Surfaces as Layered Reasoning Infrastructure]] (Finding Registry persistence need precipitated by severity scoring), [[CD-064 Goal-Focused Evaluation Framework|Goal-Focused Evaluation Framework]] (Builds on finding severity scoring for regression detection), [[CD-072 Layer-Aware Graph Health Analysis|Layer-Aware Graph Health Analysis]] (Layer-aware graph health uses CD-053 Finding Registry shape; new `graph-structural` finding category added; orphan detection outputs conform to finding-id/severity/trajectory/recurrence fields (ms-20260421-0611))
**governed-by:** [[CP-005|CP-005]] (Core-Owns-Schema first application per CP-005 principle body: Core defines CD-053 finding-tracking schema; domains populate (ms-20260421-0611))
