FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y 
RUN apt-get -y update 
RUN pip install --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
RUN pip install pygame

EXPOSE 8000

CMD ["python", "main.py"]