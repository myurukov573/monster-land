FROM python:3.12-slim

ENV SDL_AUDIODRIVER=dummy

RUN apt-get update && apt-get install -y \
    gcc \
    libsdl2-dev \
    libsdl2-mixer-dev \
    libsdl2-image-dev \
    libsdl2-ttf-dev \
    libasound2 \
    && pip install --no-cache-dir pygame \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
