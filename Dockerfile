FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Runtime/build dependencies used by the bot (ffmpeg, aria2 and Bento4/mp4decrypt).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential cmake git unzip wget ca-certificates ffmpeg aria2 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && python -m pip install -r requirements.txt

# Build Bento4 and install mp4decrypt.
RUN wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip \
    && unzip -q v1.6.0-639.zip \
    && cd Bento4-1.6.0-639 \
    && mkdir build && cd build \
    && cmake .. -DCMAKE_BUILD_TYPE=Release \
    && cmake --build . --target mp4decrypt --parallel 2 \
    && install -m 0755 mp4decrypt /usr/local/bin/mp4decrypt \
    && cd /app \
    && rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

COPY . .

# Koyeb Web Service: the bot also exposes a lightweight /health endpoint on $PORT.
CMD ["python", "modules/main.py"]
