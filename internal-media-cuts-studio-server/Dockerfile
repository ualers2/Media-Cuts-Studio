FROM mediacutstudio/ffmpeg-gpu:v1.0
    
WORKDIR /app
RUN apt-get update && apt-get install -y supervisor
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    node --version && npm --version
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel
COPY requirements.txt ./
RUN --mount=type=cache,id=pipcache,target=/root/.cache/pip \
    pip3 install --no-cache-dir -r requirements.txt
RUN --mount=type=cache,id=pipcache,target=/root/.cache/pip \
pip3 install --no-cache-dir playwright numpy llvmlite openai-whisper triton numba av && \
playwright install --with-deps
RUN pip install -U yt-dlp
COPY Studio/TiktokAutoUploader_TESTEE/tiktok_uploader/tiktok-signature/package*.json ./Studio/TiktokAutoUploader_TESTEE/tiktok_uploader/tiktok-signature/
WORKDIR /app/Studio/TiktokAutoUploader_TESTEE/tiktok_uploader/tiktok-signature
RUN npm ci && npm install playwright-chromium
WORKDIR /app
ENTRYPOINT []
COPY . ./