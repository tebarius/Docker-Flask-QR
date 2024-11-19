FROM python:slim

ARG TARGETPLATFORM
ARG BUILDPLATFORM

LABEL authors="tebarius"
LABEL version="1.4.0"
LABEL description="QR-Code-Generator-Server with Flask-App"

WORKDIR /app
COPY ./app /app/

RUN apt-get update && \
    if [ "$TARGETPLATFORM" = "linux/arm/v7" ] || [ "$TARGETPLATFORM" = "linux/386" ]; then \
        apt-get install -y --no-install-recommends zlib1g-dev libjpeg-dev gcc; \
    fi && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8002

ENV HTTP_METHOD=POST

CMD ["sh", "-c", "python ${HTTP_METHOD}-Flask-QR.py"]
