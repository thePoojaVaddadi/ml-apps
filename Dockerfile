FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p models

RUN useradd -m appuser
USER appuser

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "api.app:app"]