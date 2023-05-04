FROM python:3.10-slim-buster

ENV PATH="${PATH}:/root/.local/bin"

RUN apt-get -qq update && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false && \
    poetry self update

RUN mkdir /var/app

ARG GID=1000
ARG UID=1000

RUN groupadd -g $GID www
RUN useradd -l -u $UID -ms /bin/bash -g www www  && chown -R www:www /var/app

WORKDIR /var/app

COPY --chown=www:www pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY --chown=www:www .docker/start.sh /

EXPOSE 8000

CMD ["/bin/bash", "/start.sh"]

USER www
