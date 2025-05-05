FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libasound2 \
    libasound2-dev \
    && pip install --upgrade pip \
    && pip install pygame

EXPOSE 80

CMD ["python", "main.py"]
