FROM python:3.8

EXPOSE 5000

VOLUME ../app/:/usr/src/app/

RUN pip install pipenv

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/

COPY Pipfile Pipfile.lock /

RUN pipenv install --deploy --system --ignore-pipfile

WORKDIR /usr/src/app

CMD flask run --host=0.0.0.0