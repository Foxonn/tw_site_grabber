FROM python:3.8

RUN pip install pipenv

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/app

RUN pipenv install --deploy --system --ignore-pipfile