FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    pulseaudio \
    alsa-utils \
    libasound2 \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["python", "main.py"]
