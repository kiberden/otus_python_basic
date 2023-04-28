"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
import flask
from flask import Flask


def create_app():
    """ Создание приложения. """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    return app


app = create_app()


@app.route('/')
def index():
    """ Обработка запроса на индексную, отдаем шаблона. """
    return flask.render_template('index.html')


@app.route('/about/')
def about():
    """ Обработка запроса на страницу about, отдаем шаблона. """
    return flask.render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
