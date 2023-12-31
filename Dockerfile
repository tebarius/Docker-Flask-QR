FROM python:slim

LABEL authors="tebarius"
LABEL version="1.2.1"
LABEL description="QR-Code-Generator-Server with Flask-App"

WORKDIR /app
COPY ./app /app/

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8002

ENV HTTP_METHOD POST

CMD ["sh", "-c", "python ${HTTP_METHOD}-Flask-QR.py"]