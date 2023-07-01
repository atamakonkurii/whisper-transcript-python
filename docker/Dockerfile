FROM python:3.11.4-slim-bookworm

RUN apt-get update \
    && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install ffmpeg-python \
    && pip install pydub \
    && pip install python-dotenv \
    && pip install openai \
    && pip install pysrt \
    && pip install google-cloud-translate==2.0.1

WORKDIR /usr/src

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" /dev/null
COPY src .