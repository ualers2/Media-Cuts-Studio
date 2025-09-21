## Dockerfile otimizado apenas para o serviço de landingpage

# Use uma imagem Node.js leve
FROM node:18-slim

# Diretório de trabalho
WORKDIR /app

# Copia apenas dependências para cache de camadas
COPY ./package*.json ./

# Instala as dependências do front-end
RUN npm install --legacy-peer-deps
RUN npm install vite --save-dev
RUN npm install @stripe/stripe-js
RUN npm install framer-motion axios react-icons


# Copia todo o código da landingpage
COPY ./ ./