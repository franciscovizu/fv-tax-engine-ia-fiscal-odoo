# FV® Fiscal Copilot — Build with Gemini XPRIZE

## Competition edition

This branch contains a new competition-specific business workflow built during the Build with Gemini XPRIZE submission period. It reuses the pre-existing deterministic CFDI validation function from FV® Tax Engine as a generic technical component and adds a new AI-native operating layer using Gemini on Vertex AI.

## Category positioning

Primary category: **Small Business Services**.

Secondary relevance: **Money & Financial Access** and **Professional Services**.

The target user is a Mexican small-business finance/administration team that needs to turn CFDI operational exceptions into understandable actions without replacing its accountant or legal adviser.

## What the demo does

1. Uploads an anonymized CFDI CSV.
2. Runs deterministic fiscal-operation controls from `fv_tax_engine.py`.
3. Detects signals such as PUE + payment form 99 and PPD without a payment complement.
4. Sends only a minimal, non-identifying validation summary to Gemini through Vertex AI.
5. Gemini explains the detected issue, operational risk, and suggested review action in plain Spanish.

This is an operational control aid, not legal or tax advice.

## Google Cloud / Gemini requirement

The demo uses the Google Gen AI SDK in Vertex AI mode:

```python
client = genai.Client(vertexai=True, project=PROJECT, location=LOCATION)
client.models.generate_content(model=MODEL, contents=prompt)
```

This provides a Gemini LLM call through Google Cloud Vertex AI.

## Run locally

```bash
pip install -r xprize/requirements.txt
export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
export GOOGLE_CLOUD_LOCATION="global"
streamlit run xprize/app.py
```

Use `cfdi_demo.csv` only. Do not upload real taxpayer data to a public demo.

## Deploy to Cloud Run

From the repository root:

```bash
gcloud builds submit --tag REGION-docker.pkg.dev/PROJECT_ID/REPO/fv-fiscal-copilot -f xprize/Dockerfile .
gcloud run deploy fv-fiscal-copilot \
  --image REGION-docker.pkg.dev/PROJECT_ID/REPO/fv-fiscal-copilot \
  --region REGION \
  --allow-unauthenticated \
  --set-env-vars GOOGLE_CLOUD_PROJECT=PROJECT_ID,GOOGLE_CLOUD_LOCATION=global
```

Grant the Cloud Run runtime service account only the minimum Vertex AI permissions required for Gemini inference.

## Pre-existing work disclosure

The deterministic CFDI rule engine predates this competition-specific branch. For this XPRIZE edition it is treated as a reusable technical component. The new work is the AI-native business workflow, Gemini/Vertex AI explanation layer, user-facing demo, Cloud Run packaging, competition positioning, and evidence plan.

This disclosure should also be copied into the Devpost submission so judges can distinguish reused components from work created for this competition.

## Submission evidence to prepare

- Public Cloud Run demo URL.
- Repository URL pointing to this branch.
- <3 minute public YouTube/Vimeo/Youku demo video.
- Screenshot or log proving Gemini/Vertex AI calls.
- Clear explanation of AI-native operations.
- Business viability evidence: target customer, pricing hypothesis, real customer/user validation if available, and any eligible revenue/expense evidence generated during the competition period.
- Category-impact argument focused on reducing manual fiscal-control work for Mexican SMBs.

## Current status

- Competition branch: created.
- Gemini/Vertex AI call: implemented in code.
- Streamlit demo: implemented in code.
- Cloud Run container: implemented in code.
- Live deployment: pending Google Cloud credentials/project configuration.
- Devpost registration/submission: must be completed in the user's authenticated Devpost session.
