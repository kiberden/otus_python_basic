# Запускать через docker-compose командой docker-compose up.
# Доступ по адресу localhost:8000
FROM python:3.10-slim

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get -qq update && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry self update

WORKDIR /main

COPY pyproject.toml ./
RUN poetry install --no-root

COPY start.sh ./
RUN chmod +x ./start.sh

EXPOSE 8000

CMD ["/bin/bash", "start.sh"]
