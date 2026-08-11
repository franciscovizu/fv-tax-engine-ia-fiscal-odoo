# Google Cloud / Vertex AI deployment checklist

This checklist is for the Build with Gemini XPRIZE competition branch.

## Before deployment

1. Use an eligible Google Cloud project.
2. Confirm billing only if Google Cloud explicitly requires it for the selected project/service.
3. Enable the APIs required for Cloud Run, Cloud Build/Artifact Registry and Vertex AI.
4. Authenticate with the Google account that owns or has access to the project.
5. Set the runtime environment variables:
   - `GOOGLE_CLOUD_PROJECT`
   - `GOOGLE_CLOUD_LOCATION=global`
   - optional `GEMINI_MODEL=gemini-2.5-flash`

## Deploy

Use the commands documented in `xprize/README.md` after replacing placeholders with the actual project, region and Artifact Registry repository.

## Runtime permissions

Grant the Cloud Run runtime service account only the minimum permission needed to call Vertex AI/Gemini. Do not store service-account keys, API keys or credentials in this repository.

## Judge verification

After deployment, verify all of the following from a private/incognito browser window:

- public URL opens without sign-in;
- bundled synthetic sample loads;
- CFDI control results render;
- a non-green item can call **Explicar con Gemini** successfully;
- Gemini returns detection, operational risk and next review action;
- no RFC, UUID, taxpayer name or real accounting data appears in the request or UI;
- the public URL remains stable long enough for judging.

## Evidence to capture

Capture one screenshot or short screen recording showing:

1. the public Cloud Run URL;
2. the synthetic sample loaded;
3. a detected non-green exception;
4. a successful Gemini explanation;
5. Google Cloud/Vertex AI evidence sufficient to show that the request is powered by Gemini on Vertex AI, without exposing secrets.

## Do not publish

Never commit or expose:

- service-account JSON files;
- access tokens;
- API keys;
- real taxpayer data;
- RFCs or UUIDs from production;
- confidential accounting records.

## Final handoff to Devpost

Once the public URL works, copy it into `SUBMISSION_DRAFT.md`, record the demo video, publish the video, then paste the final narrative, repository branch URL, live demo URL, video URL and pre-existing-work disclosure into Devpost.
