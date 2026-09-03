# FV® Tax Engine | WebMCP Challenge Edition

FV-ID VIZF850813D46

Copyright (c) 2026 José Francisco Villaseñor Zúñiga (FV®)

## Challenge scope

This branch isolates the WebMCP Challenge work from the pre-existing FV® Tax Engine foundation.

Pre-existing work includes the Python CFDI validation demo, anonymized fiscal data, SAT/Odoo concepts, and deterministic fiscal rules.

New work for the WebMCP Challenge includes:

- `webmcp/index.html`, a browser-native WebMCP demo.
- Four tools registered through `document.modelContext.registerTool()`:
  - `list_cfdi_findings`
  - `analyze_cfdi`
  - `summarize_fiscal_risk`
  - `prepare_odoo_action`
- A human approval gate for proposed Odoo follow-up actions.
- A static UI showing the same deterministic PUE/PPD findings used by the Python fiscal demo.

## How to run

The WebMCP demo is a static HTML application with no build step.

1. Serve `webmcp/index.html` from any static host.
2. Open the hosted page in ChatGPT's in-app browser or in a WebMCP-enabled Chrome build.
3. Ask the agent to discover and use the registered WebMCP tools.

## Suggested judge tests

- Ask for all red CFDI findings.
- Ask for a summary of green, yellow, and red risks.
- Ask the agent to analyze a sample PUE CFDI using payment form 99.
- Ask the agent to prepare an Odoo follow-up for the red finding.
- Verify that the proposed Odoo action appears as `PENDING_HUMAN_APPROVAL` and is not executed automatically.

## Deterministic fiscal rules demonstrated

- Missing mandatory fields => `ROJO`.
- `PUE` with payment form `99` => `ROJO`.
- `PPD` without payment complement => `AMARILLO`.
- Otherwise => `VERDE` in the basic demo.

## Safety and professional control

This is an evaluation/demo environment using anonymized records. It does not write to a production Odoo database and does not make autonomous tax filings or tax conclusions. Sensitive accounting actions remain behind explicit human approval.

## License

The `webmcp-challenge` branch is provided under the MIT License in this branch's root `LICENSE` file. The historical `main` branch retains its separate pre-existing licensing terms.
