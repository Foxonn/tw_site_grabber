FROM python:3.8

RUN pip install pipenv

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/

COPY Pipfile Pipfile.lock /

RUN pipenv install --deploy --system --ignore-pipfile

WORKDIR /usr/src/app