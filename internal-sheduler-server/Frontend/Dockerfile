## Dockerfile otimizado apenas para o serviço de landingpage

# Use uma imagem Node.js leve
FROM node:18-slim

# Diretório de trabalho
WORKDIR /app

RUN if [ -f /etc/apt/sources.list ]; then \
      sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
      sed -i 's|http://security.debian.org/|http://archive.debian.org/|g' /etc/apt/sources.list; \
    fi && \
    apt update && \
    apt install -y curl unzip && \
    curl -s -o ngrok.zip https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip && \
    unzip ngrok.zip -d /usr/local/bin && \
    rm ngrok.zip
    
# Copia apenas dependências para cache de camadas
COPY ./package*.json ./

# Instala as dependências do front-end
RUN npm install --legacy-peer-deps
RUN npm i vite --save-dev

# Copia todo o código da landingpage
COPY ./ ./