FROM python:3.6-alpine

WORKDIR /src

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN set -ex &&\
    apk add --no-cache --virtual .build-deps gcc musl-dev &&\
    apk add --no-cache postgresql-dev python3-dev &&\
    pip install pipenv && pipenv install --deploy --system &&\
    apk del --no-cache .build-deps

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]