""" Приложение на flask. """
import os

import flask
from flask import Flask


def create_app():
    """ Создание приложения. """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=os.getenv('SECRET_KEY'))

    return app


app = create_app()


@app.route('/')
def index():
    """ Обработка запроса на индексную, отдаем шаблона. """
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run()
