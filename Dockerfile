FROM python:3.11-slim

WORKDIR /app

COPY app/ app/
COPY sample.log .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "app.main", "sample.log"]
