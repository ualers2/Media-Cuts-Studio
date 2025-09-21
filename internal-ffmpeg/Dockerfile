# FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04
FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libfdk-aac2 libcudnn9-cuda-12 libcudnn9-dev-cuda-12 cuda-toolkit-12-1 \
    libdrm2 libxcb1 libx11-6 libvdpau1 \
    libgl1 libglib2.0-0 libgl1-mesa-glx libsm6 libxrender1 libxext6 \
    libxcomposite1 libxdamage1 libxss1 libxtst6 \
    automake build-essential cmake git pkg-config \
    libass-dev libfreetype6-dev libtool libvorbis-dev libvpx-dev \
    libx264-dev libx265-dev libnuma-dev libfdk-aac-dev \
    libmp3lame-dev libopus-dev libxvidcore-dev libfontconfig1-dev \
    libsoxr-dev yasm nasm zlib1g-dev libopenjp2-7-dev \
    libwebp-dev libfribidi-dev libfreetype-dev libfontconfig-dev \
    libharfbuzz-dev zlib1g-dev libdav1d-dev \
    frei0r-plugins libopengl-dev libgl1-mesa-dev libglu1-mesa-dev \
    frei0r-plugins-dev meson ninja-build \
    libpthread-stubs0-dev libglfw3-dev libjansson-dev \
    libmujs-dev libpng-dev libavutil-dev libavformat-dev libswscale-dev \
    curl gnupg2 ca-certificates wget unzip \
    nginx redis-server jq fonts-liberation \
    build-essential pkg-config libffi-dev libssl-dev libatlas-base-dev \
    libblas-dev liblapack-dev python3 python3-pip python3-dev \
    libatk1.0-0 libatk-bridge2.0-0 libcups2 libatspi2.0-0 libnss3 libnss3-dev \
    libgdk-pixbuf2.0-dev libappindicator3-1 libsecret-1-dev libdbus-glib-1-2 \
    libpango-1.0-0 libfontconfig1 libexpat1 libgcc1 libc6 libnspr4 \
    default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/* && \
    ldconfig
# RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-keyring_1.1-1_all.deb
# RUN dpkg -i cuda-keyring_1.1-1_all.deb

WORKDIR /app/ffmpeg
RUN mkdir -p src bin
RUN git clone https://git.ffmpeg.org/ffmpeg.git src
WORKDIR /app
RUN git clone https://git.videolan.org/git/ffmpeg/nv-codec-headers.git /usr/src/nv-codec-headers && \
    cd /usr/src/nv-codec-headers && \
    make && \
    make install 
RUN git clone https://github.com/Netflix/vmaf.git vmaf
WORKDIR /app/vmaf/libvmaf
RUN find . -exec touch {} +
RUN meson setup build --buildtype release \
    && ninja -C build \
    && ninja -C build install \
    && ldconfig
WORKDIR /app/ffmpeg/src
RUN PKG_CONFIG_PATH="/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/local/lib/pkgconfig" \
    ./configure --prefix="$(pwd)/../bin" \
    --extra-cflags="-I/usr/local/include" \
    --extra-ldflags="-L/usr/local/lib" \
    --extra-libs="-lpthread -lm" \
    --enable-version3 \
    --disable-shared \
    --enable-static \
    --enable-gpl --enable-nonfree \
    --enable-libass --enable-fontconfig \
    --enable-libfreetype --enable-libfontconfig \
    --enable-libharfbuzz --enable-filter=drawtext \
    --enable-libvorbis --enable-frei0r \
    --enable-libvmaf --enable-libfribidi \
    --enable-libvpx --enable-libx264 \
    --enable-libx265 --enable-libmp3lame \
    --enable-libopus --enable-libfdk-aac \
    --enable-libxvid --enable-libsoxr \
    --enable-libopenjpeg --enable-libwebp \
    --enable-cuda --enable-cuvid \
    --enable-nvdec --enable-nvenc \
    --enable-filter=xfade \
    --enable-opengl \
    --enable-frei0r \
    --enable-filter=gltransition \
    --enable-libdav1d --enable-bsf=hevc_mp4toannexb
RUN make -j$(nproc) && make install && ldconfig 
RUN cp /app/ffmpeg/bin/bin/ffmpeg /usr/local/bin/ffmpeg && \
    chmod +x /usr/local/bin/ffmpeg

ENV LD_LIBRARY_PATH=/usr/local/bin/lib:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH

RUN --mount=type=cache,id=pipcache,target=/root/.cache/pip \
pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

ENTRYPOINT ["ffmpeg"]
