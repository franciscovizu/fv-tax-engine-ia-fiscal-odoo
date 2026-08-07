FROM python:3.12-slim

WORKDIR /app

COPY xprize/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY fv_tax_engine.py /app/fv_tax_engine.py
COPY cfdi_demo.csv /app/cfdi_demo.csv
COPY xprize/app.py /app/app.py

ENV PORT=8080
CMD ["sh", "-c", "streamlit run /app/app.py --server.port=${PORT} --server.address=0.0.0.0 --server.headless=true"]
