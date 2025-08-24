# Basis-Image mit Python 3.11
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere alle Dateien ins Arbeitsverzeichnis
COPY . /app

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Starte das Add-on mit run.py
CMD ["python", "run.py"]
