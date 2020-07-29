FROM python:3.8

EXPOSE 5000

RUN python -m pip install --upgrade pip

RUN pip install pipenv

RUN mkdir -p /usr/src/app

COPY Pipfile Pipfile.lock /usr/src/

WORKDIR /usr/src/

RUN pipenv install --deploy --system --ignore-pipfile

CMD flask run --host=0.0.0.0
