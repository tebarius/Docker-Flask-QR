FROM python:slim

LABEL authors="tebarius"
LABEL version="1.0"
LABEL description="Simple QR-Code-Generator-Server"

WORKDIR /app
RUN mkdir templates
COPY ./templates /app/templates/
COPY ./Flask-QR.py ./requirements.txt /app/

#RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "Flask-QR.py"]