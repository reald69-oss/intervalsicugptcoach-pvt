# Regression Report: Loss of Deterministic Tool Rendering in GPT-5.5

## Background

I am the developer of **www.montis.icu**, a production coaching platform built on top of ChatGPT GPTs and OpenAPI tools.

Montis does **not** ask the model to generate coaching from scratch.

Instead, the application performs all analysis externally and returns a **validated semantic graph** representing the complete coaching state.

The model's responsibility is solely to render this validated semantic graph into the final report according to a supplied rendering contract.

This architecture worked reliably with GPT-5.4.

---

# Current Architecture

```
User
   ↓
OpenAPI Tool
   ↓
Railway Backend
   ↓
Validated Semantic Graph
   ↓
ChatGPT renders report
```

Important points:

* The semantic graph is already fully validated.
* Coaching decisions have already been computed.
* Report structure is already defined.
* The model is **not** expected to invent, improve or reinterpret content.
* The model is expected to execute a rendering contract.

---

# Previous Behaviour (GPT-5.4)

GPT-5.4 consistently behaved as though the semantic graph and its renderer instructions formed an executable rendering specification.

It would:

* preserve section ordering
* preserve report hierarchy
* preserve tables
* preserve report titles
* avoid introducing additional summaries
* faithfully render the supplied report structure

This behaviour allowed deterministic production reporting while still benefiting from natural-language rendering.

---

# Current Behaviour (GPT-5.5)

GPT-5.5 no longer behaves as a renderer.

Instead it behaves as a conversational assistant.

Typical behaviour now includes:

* introducing "Executive Summary"
* renaming report sections
* merging independent report layers
* omitting supplied sections
* rewriting validated coaching conclusions
* replacing structured output with generic narrative

This occurs even when:

* renderer instructions are supplied
* system instructions explicitly prohibit summarisation
* the semantic graph already defines report structure
* the backend has already completed all reasoning

The model appears to reinterpret the validated application state instead of rendering it.

---

# Why this is a Production Problem

For applications like Montis, the report itself is part of the application.

It is not merely prose.

Each section corresponds to a validated analysis layer:

* Training Load
* Physiology
* Performance Intelligence
* Adaptation
* Adaptive Decisions

These layers intentionally remain separate.

When GPT merges or rewrites them, it changes the presentation of validated application state.

This reduces consistency and undermines user trust in deterministic reporting.

---

# Existing Workarounds Attempted

I have attempted:

* renderer_instructions
* response_mode flags
* verbatim instructions
* semantic-only payloads
* alternative OpenAPI descriptions
* operationId changes
* stronger GPT system prompts

None restore the previous rendering fidelity.

The model continues to rewrite the supplied structure.

---

# Feature Request

Please provide an explicit execution mode for tool outputs containing validated structured data.

Conceptually:

```
Tool Output
        ↓
Renderer Contract
        ↓
Execute Exactly
```

rather than

```
Tool Output
        ↓
Interpret
Summarise
Rewrite
Generate
```

This capability would allow applications that already perform deterministic reasoning externally to preserve deterministic presentation.

---

# Why This Matters

This is not a request for "better prompt following."

It is a request to preserve the distinction between:

* reasoning
* rendering

Many production systems already separate those responsibilities.

The current behaviour makes it difficult to use GPT as the final rendering layer for validated application state.

GPT-5.4 demonstrated behaviour much closer to deterministic rendering.

GPT-5.5 instead behaves as a conversational editor, even when the application explicitly provides the complete report structure.

I believe an explicit rendering mode for validated tool outputs would solve this class of application while leaving the default conversational behaviour unchanged for general users.
