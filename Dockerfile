FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "I18N CHECK" && ls -la /app/i18n && test -f /app/i18n/fr.json

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]

