FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  # Certifique-se de que `gunicorn` está no arquivo!

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "core.wsgi:application"]