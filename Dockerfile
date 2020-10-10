# Dockerfile
FROM python:3.8
RUN pip install "poetry" "celery[redis]"
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN poetry install