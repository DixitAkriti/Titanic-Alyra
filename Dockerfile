FROM python:3.9.9-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends\
    # python3-dev \
    curl\
    g++\
    && rm -rf /var/lib/apt/lists/*
   
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . /app/.
