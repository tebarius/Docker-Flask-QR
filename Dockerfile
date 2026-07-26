FROM python:3.14-alpine
LABEL authors="tebarius"
LABEL description="QR-Code-Generator-Server with Flask-App"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV HTTP_METHOD=POST

WORKDIR /app
COPY requirements.txt .

RUN apk upgrade --no-cache --available \
    && python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./app /app/
RUN  adduser -D -H -u 1000 -s /bin/sh qr \
    && chown -R qr:qr /app

USER qr

EXPOSE 8002

HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD  wget -q -O /dev/null http://127.0.0.1:8002/health || exit 1

CMD ["sh", "-c", "python ${HTTP_METHOD}-Flask-QR.py"]
