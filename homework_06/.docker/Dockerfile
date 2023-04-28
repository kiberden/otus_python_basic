#FROM python:3.10-slim
FROM tiangolo/uwsgi-nginx-flask:python3.10

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get -qq update && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry self update

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

#COPY .docker/uwsgi.ini uwsgi.ini
COPY .docker/prestart.sh prestart.sh
