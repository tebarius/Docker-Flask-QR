FROM ubuntu:latest
LABEL authors="tebarius"

ENTRYPOINT ["top", "-b"]