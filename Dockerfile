FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt /app/requirements.txt

ENV PYTHONPATH=/

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY app/ /app/

EXPOSE 5000

CMD ["python", "main.py"]

