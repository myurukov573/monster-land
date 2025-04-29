FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pygame

EXPOSE 8000

CMD ["python", "main.py"]