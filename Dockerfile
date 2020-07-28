FROM python:3.8

RUN pip install pipenv

RUN mkdir -p /usr/src/app

COPY ${pwd}Pipfile ${pwd}Pipfile.lock /usr/src/

WORKDIR /usr/src/

RUN pipenv install --deploy --system --ignore-pipfile

WORKDIR /usr/src/app