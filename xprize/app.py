"""FV Fiscal Copilot — Build with Gemini XPRIZE demo.

A lightweight Streamlit app that combines the deterministic FV Tax Engine
CFDI checks with Gemini on Vertex AI to explain detected risks in plain
business language. No credentials or taxpayer data are stored in the repo.
"""

from __future__ import annotations

import csv
import io
import os

import streamlit as st
from google import genai

from fv_tax_engine import evaluate


MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")


def gemini_client() -> genai.Client:
    if not PROJECT:
        raise RuntimeError("GOOGLE_CLOUD_PROJECT is not configured")
    return genai.Client(vertexai=True, project=PROJECT, location=LOCATION)


def explain_with_gemini(row: dict[str, str], semaforo: str, resultado: str) -> str:
    safe_fields = {
        "tipo": row.get("tipo", ""),
        "metodo_pago": row.get("metodo_pago", ""),
        "forma_pago": row.get("forma_pago", ""),
        "tiene_complemento": row.get("tiene_complemento", ""),
        "semaforo": semaforo,
        "resultado_regla": resultado,
    }
    prompt = f"""
You are a Mexican SMB fiscal-operations copilot. Explain the following CFDI
validation result in concise Spanish for a finance manager. Do not invent tax
facts, legal conclusions, dates, amounts, RFCs, or SAT rules that are not in
the input. State that this is an operational control signal, not legal advice.
Give: (1) what was detected, (2) operational risk, (3) next review action.

Input: {safe_fields}
"""
    response = gemini_client().models.generate_content(model=MODEL, contents=prompt)
    return response.text or "Sin explicación disponible."


def parse_csv(uploaded_file) -> list[dict[str, str]]:
    text = uploaded_file.getvalue().decode("utf-8-sig")
    return list(csv.DictReader(io.StringIO(text)))


st.set_page_config(page_title="FV Fiscal Copilot", page_icon="🧾", layout="wide")
st.title("FV® Fiscal Copilot — Gemini XPRIZE")
st.caption("CFDI operational controls + Gemini explanations for Mexican small businesses")

uploaded = st.file_uploader("Carga un CSV CFDI anonimizado", type=["csv"])

if uploaded:
    rows = parse_csv(uploaded)
    st.write(f"CFDI analizados: {len(rows)}")

    for index, row in enumerate(rows, start=1):
        semaforo, resultado = evaluate(row)
        with st.expander(f"CFDI {index} · {semaforo} · {resultado}", expanded=semaforo != "VERDE"):
            st.json({
                "tipo": row.get("tipo", ""),
                "metodo_pago": row.get("metodo_pago", ""),
                "forma_pago": row.get("forma_pago", ""),
                "tiene_complemento": row.get("tiene_complemento", ""),
                "semaforo": semaforo,
                "resultado": resultado,
            })
            if st.button("Explicar con Gemini", key=f"gemini-{index}"):
                try:
                    with st.spinner("Gemini está preparando la explicación..."):
                        explanation = explain_with_gemini(row, semaforo, resultado)
                    st.write(explanation)
                except Exception as exc:
                    st.error(f"No fue posible llamar a Gemini/Vertex AI: {exc}")
else:
    st.info("Usa cfdi_demo.csv como archivo de demostración. No cargues CFDI reales con datos sensibles.")
