ARG BASE_CONTAINER=python:3.11.1-slim-bullseye

FROM --platform=linux/amd64 $BASE_CONTAINER

LABEL maintainer=ManoelSilva

USER root
RUN apt-get update && apt-get install -y && apt-get clean

WORKDIR /receiver

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY /src ./src

CMD ["python", "-m", "src"]