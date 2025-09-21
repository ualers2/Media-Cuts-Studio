# Dockerfile (recomendado)
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

WORKDIR /app

# Se você tem requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN apt update && \
    apt install -y curl git unzip 
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    node --version && npm --version

# Copia apenas package.json da pasta que precisa do npm
COPY Uploaders/TiktokAutoUploader/tiktok_uploader/tiktok-signature/package*.json ./Uploaders/TiktokAutoUploader/tiktok_uploader/tiktok-signature/

WORKDIR /app/Uploaders/TiktokAutoUploader/tiktok_uploader/tiktok-signature


RUN npm ci \
    && npm install -D playwright-chromium \
    && npm install -D playwright-chromium@1.54.2 \
    && npm install -D playwright \
    && npx --yes playwright install \

    && npx playwright --version 


WORKDIR /app

COPY . ./