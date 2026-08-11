# Build with Gemini XPRIZE — Submission Draft

## Project title
FV® Fiscal Copilot

## One-line description
AI-native fiscal-operations copilot that combines deterministic CFDI controls with Gemini on Vertex AI to explain exceptions and next actions for Mexican small-business finance teams.

## Primary category
Small Business Services

## Problem
Mexican SMB finance and administration teams spend significant manual effort reviewing CFDI operational consistency. Technical exceptions involving payment method, payment form and payment complements can be easy to miss or difficult for non-specialists to interpret.

## Solution
FV® Fiscal Copilot uses a two-layer workflow. First, a deterministic rules engine identifies operational control signals in anonymized CFDI data. Second, Gemini on Vertex AI receives only a minimal non-identifying summary and explains in plain Spanish what was detected, the operational risk and the next review action. Human review remains the final decision point.

## Why AI is essential
The deterministic layer can flag an exception, but the value of the AI-native workflow is turning structured technical output into contextual, understandable and actionable guidance for a finance manager. Gemini is embedded directly in the exception-handling workflow rather than added as a generic chatbot.

## Impact
The project is designed to reduce repetitive fiscal-control work for Mexican SMBs, shorten the time required to understand exceptions and improve the consistency of human review. The broader opportunity is to make professional-grade fiscal controls more accessible to small businesses that do not have large internal tax or ERP teams.

## Business viability hypothesis
Target users: Mexican SMB owners, finance managers, administrators, accountants and Odoo implementation teams.

Potential commercial model:
- entry tier for periodic CFDI control;
- professional tier for recurring monitoring and dashboards;
- ERP integration tier for Odoo workflows and controlled layouts.

The competition demo is intentionally narrow and safe; the broader product roadmap includes XML extraction, payment-complement relationships, IVA/ISR working papers, dashboards and controlled Odoo integration.

## Technology
- Python
- Streamlit
- Google Gen AI SDK
- Gemini on Vertex AI
- Google Cloud Run packaging
- deterministic FV® CFDI validation engine

## Privacy and safety
The public demo uses synthetic/anonymized data. The Gemini prompt excludes RFCs, UUIDs, taxpayer names, credentials and real accounting records. The product is an operational-control aid, not tax, accounting or legal advice.

## Pre-existing work disclosure
The deterministic CFDI rule engine predates the Build with Gemini XPRIZE competition branch and is reused as a generic technical component. Competition-specific work includes the Gemini/Vertex AI explanation layer, AI-native exception workflow, Streamlit user interface, Cloud Run packaging, XPRIZE positioning and submission evidence.

## Demo flow for judges
1. Open the public demo.
2. Select **Usar muestra incluida**.
3. Review detected green/yellow/red CFDI control signals.
4. Open a non-green exception.
5. Press **Explicar con Gemini**.
6. Observe the plain-Spanish explanation: detection, operational risk and next review action.
7. Confirm that no identifying taxpayer data is sent to Gemini.

## Video script — target 2:15 to 2:45

### 0:00–0:20 — Problem
“Mexican small businesses process CFDI every day, but operational inconsistencies can be difficult and time-consuming to review manually. FV Fiscal Copilot helps finance teams detect and understand those exceptions.”

### 0:20–0:45 — Architecture
“The workflow has two layers. First, deterministic FV rules detect known control signals. Then Gemini on Vertex AI turns the structured result into a concise explanation and recommended review action in Spanish.”

### 0:45–1:35 — Live demo
“Here I use only the bundled synthetic sample. The engine processes the CFDI rows and highlights exceptions. I open one detected issue and request an explanation from Gemini. The model receives only minimal, non-identifying fields — no RFC, UUID, taxpayer name or real accounting record.”

### 1:35–2:05 — AI-native value
“The rules engine tells us that something needs attention. Gemini makes that signal operationally useful by explaining what happened, why it matters and what the finance team should review next. Human professional judgment remains in control.”

### 2:05–2:35 — Impact and business
“The target is Mexican SMB finance teams and accounting professionals. The goal is to reduce repetitive fiscal-control work and make technical exceptions easier to act on. The broader roadmap connects these controls to recurring monitoring, dashboards and Odoo workflows.”

### 2:35–2:45 — Close
“FV Fiscal Copilot: deterministic fiscal controls, Gemini-powered explanations, and human review for safer small-business finance operations.”

## Final submission checklist

### Completed in repository
- [x] Competition-specific branch `xprize-gemini-2026`
- [x] Gemini/Vertex AI integration in code
- [x] Streamlit demonstration interface
- [x] Bundled synthetic demo workflow
- [x] Cloud Run Dockerfile
- [x] Requirements file
- [x] Privacy-by-design prompt fields
- [x] Pre-existing-work disclosure
- [x] Root README aligned to XPRIZE
- [x] Draft Devpost narrative
- [x] <3-minute video script

### Requires external/authenticated action
- [ ] Configure an eligible Google Cloud project and Vertex AI authentication
- [ ] Deploy and verify a public Cloud Run URL, or provide another competition-eligible accessible demo
- [ ] Capture proof that the Gemini/Vertex AI call works in the deployed demo
- [ ] Record and publish the <3-minute demo video
- [ ] Paste final narrative, links and disclosure into the authenticated Devpost submission
- [ ] Submit before the competition deadline

## Final verification before Submit
- Public demo opens without authentication errors.
- Bundled sample loads immediately.
- At least one non-green exception can call Gemini successfully.
- No secret, credential or real taxpayer data appears in the repository, video or demo.
- Repository link points to the `xprize-gemini-2026` branch.
- Video is publicly viewable by judges.
- Devpost disclosure matches the repository disclosure.
