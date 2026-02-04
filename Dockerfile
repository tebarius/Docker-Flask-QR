FROM python:3.14-slim
LABEL authors="tebarius"
LABEL description="QR-Code-Generator-Server with Flask-App"

ARG TARGETPLATFORM
ARG BUILDPLATFORM
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HTTP_METHOD=POST

RUN apt-get update && \
    if [ "$TARGETPLATFORM" = "linux/arm/v7" ] || [ "$TARGETPLATFORM" = "linux/386" ]; then \
        apt-get install -y --no-install-recommends zlib1g-dev libjpeg-dev gcc; \
    fi && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./app /app/

RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && useradd -m -u 1000 qr \
    && chown -R qr:qr /app

USER qr

EXPOSE 8002

CMD ["sh", "-c", "python ${HTTP_METHOD}-Flask-QR.py"]
