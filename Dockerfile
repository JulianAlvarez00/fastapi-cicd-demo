FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

# Render específico - usar variable de entorno PORT
CMD uvicorn src.main:app --host 0.0.0.0 --port $PORT