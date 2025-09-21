FROM python:3.11

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install yt_dlp
WORKDIR /app
COPY . .

