FROM python:3.11-slim

RUN pip install paho-mqtt

COPY run.py /run.py

CMD ["python", "/run.py"]
