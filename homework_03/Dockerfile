# Запускать через docker-compose командой docker-compose up.
# Доступ по адресу localhost:8000
# Билдим образ docker build -t otus-app .
# Запускаем образ docker run -it -p 8000:8000 otus-app
FROM python:3.10-slim

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get -qq update && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry self update

RUN mkdir project
WORKDIR /project

COPY main.py ./
COPY pyproject.toml ./

RUN poetry install --no-root

EXPOSE 8000

CMD uvicorn main:route --host=0.0.0.0 --port 8000
