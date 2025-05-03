FROM python:3.11-slim

WORKDIR /app

COPY api/ ./api/
COPY data/ ./data/
COPY api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]