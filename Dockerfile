FROM ubuntu:22.04

EXPOSE 5000

RUN apt update && \
    apt install -y \
        build-essential \
        python3 \
        python3-venv \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt && \
    adduser --gecos '' --disabled-password --home=/LibreTranslate libretranslate

USER libretranslate
WORKDIR /LibreTranslate

RUN python3 -m venv .venv && \
    . .venv/bin/activate && \
    pip install -U pip setuptools && \
    pip install -U wheel && \
    pip install libretranslate && \
    pip cache purge

CMD [".venv/bin/libretranslate", "--load-only", "es,en", "--host", "0.0.0.0"]
