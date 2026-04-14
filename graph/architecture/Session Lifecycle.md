---
type: architecture
tags: [architecture, lifecycle]
generated: 2026-04-13
---

# Session Lifecycle

How a Meridian session flows from start to close. This is the runtime architecture — what happens when, and what talks to what.

## Session Start

```mermaid
sequenceDiagram
    participant CC as Claude Code Platform
    participant Hook as SessionStart Hook
    participant CSA as CSA (Orchestrator)
    participant STA as STA Agent
    participant WM as Working Memory
    participant RAG as Corpus (mcp-local-rag)
    participant FS as File System

    CC->>Hook: Session begins
    Hook->>FS: Read active manifests
    Hook->>CSA: Inject session identity + state

    alt New Session
        CSA->>FS: Create manifest in active/
        CSA->>CSA: Present mode selection to human
    else Continuing Session
        CSA->>FS: Add CC segment to manifest
    end

    CSA->>STA: Launch (background)
    STA->>FS: Scan closed/ for last session
    STA->>FS: Read prior KC summary or STA summary
    STA->>FS: Check notification file (exists? size?)
    STA->>FS: Create session summary file
    STA-->>CSA: Health report

    CSA->>CSA: Surface health report to human

    opt Notification file exists
        CSA->>FS: Read notification file
        CSA->>CSA: Present findings to human
        CSA->>FS: Write checkpoint
    end
```

## Exchange Cycle (Every Response)

```mermaid
sequenceDiagram
    participant Human
    participant Hook as UserPromptSubmit Hook
    participant CSA as CSA (Orchestrator)
    participant STA as STA Agent
    participant WM as Working Memory
    participant RAG as Corpus (mcp-local-rag)
    participant KSA as KSA Agent
    participant LWA as LWA Agent

    Human->>Hook: Sends message
    Hook->>FS: Check signal.md
    
    alt Signal file has content
        Hook->>CSA: Inject nudge
        CSA->>CSA: Clear signal.md
        CSA->>WM: Ambient query (sta-gap entries)
        
        opt Gap entries found
            CSA->>KSA: Launch deep search
            KSA->>RAG: Grep + semantic search
            KSA-->>CSA: Findings + search instructions
            CSA->>RAG: Execute semantic queries
            CSA->>WM: Write enrichment
        end
    end

    opt New topic detected
        CSA->>WM: Ambient query (topic-based)
        CSA->>RAG: Ambient query (topic-based)
    end

    CSA->>CSA: Process human message + context
    CSA->>Human: Respond

    opt Layer writes needed
        CSA->>LWA: Delegate writes
        LWA->>FS: Write files + CHANGELOG
        LWA-->>CSA: Confirm
    end

    CSA->>STA: Feed exchange summary
    STA->>STA: Tier 1 gap detection
    
    alt New topics found
        STA->>FS: Write signal.md
        STA->>WM: Write gap content
    end
    
    STA->>FS: Update session summary
    STA-->>CSA: NEXT_ACTION callback
    CSA->>WM: Surface write (sta-context)

    participant FS as File System
```

## Session Close (Meridian Close)

```mermaid
sequenceDiagram
    participant Human
    participant CSA as CSA (Orchestrator)
    participant FS as File System
    participant Git as Git

    Human->>CSA: "close" / "meridian close"
    
    CSA->>FS: Update manifest (Status → closed)
    CSA->>FS: Update manifest (KC Status → pending)
    CSA->>FS: Move manifest: active/ → closed/
    CSA->>FS: Clear signal.md
    
    CSA->>Git: git add -A
    CSA->>Git: git commit "checkpoint: session close"
    CSA->>Git: git push origin main
    
    CSA->>Human: Session closed, checkpoint committed

    Note over CSA,FS: No STA delegation at close (CD-007)
    Note over CSA,FS: No KC at close — runs in pipeline between sessions
    Note over CSA,FS: No domain housekeeping — deferred to KC pipeline
```

## Between-Session Pipeline (Hub Sleep Mode)

```mermaid
flowchart TD
    subgraph Phase1["Phase 1: Ingest"]
        A1[Extract transcripts] --> A2[Validate corpus]
        A2 --> A3[Re-ingest stale items]
    end

    subgraph Phase2["Phase 2: Analyze"]
        B1[KC Pipeline — pending sessions] --> B2[Structural Audit]
        B2 --> B3[Graph Gap Detection]
    end

    subgraph Phase3["Phase 3: Synthesize"]
        C1[Generate Core Graph] --> C2[Cross-domain pattern detection]
        C2 --> C3[Finding Registry update]
        C3 --> C4[Generate dashboards]
    end

    subgraph Phase4["Phase 4: Remediate"]
        D1{Finding type?}
        D1 -->|Mechanical| D2[Auto-fix]
        D1 -->|Substantive| D3[Queue for human review]
    end

    subgraph Phase5["Phase 5: Report"]
        E1[Write notification files]
        E2[Summary: what changed, what needs judgment]
    end

    Phase1 --> Phase2 --> Phase3 --> Phase4 --> Phase5
```

## Component Topology

```mermaid
flowchart TB
    subgraph Platform["Claude Code Platform"]
        CC[Claude Code Runtime]
        Hooks[Hooks Engine]
        CC --> Hooks
    end

    subgraph Orchestrator["Session Orchestrator"]
        CSA[CSA]
    end

    subgraph Agents["Agent Services"]
        STA[STA — Session Awareness]
        LWA[LWA — Layer Writes]
        KSA[KSA — Knowledge Search]
        KC[KC — Knowledge Capture]
        DWA[DWA — Core Writes]
    end

    subgraph MCP["MCP Servers"]
        RAG[mcp-local-rag — Corpus Index]
        WM[working-memory — Ambient Surface]
    end

    subgraph Storage["File System"]
        KOS[".kos/ — Core Infrastructure"]
        Layers["Four Layers — Domain Knowledge"]
        Meridian[".meridian/ — Session Artifacts"]
        Hub["Hub — Cross-domain Services"]
    end

    subgraph Viz["Observability"]
        Obsidian["Obsidian Vault — Graph + Diagrams"]
        Dashboard["Dashboard — Session Analytics"]
    end

    Hooks --> CSA
    CSA --> STA
    CSA --> LWA
    CSA --> KSA
    CSA --> KC
    CSA --> DWA

    CSA --> RAG
    CSA --> WM
    STA --> WM
    KSA --> RAG

    LWA --> Layers
    DWA --> KOS
    STA --> Meridian
    
    Hub --> Storage
    KOS --> Obsidian
    Layers --> Obsidian
    KOS --> Dashboard
```
