"""
Домашнее задание №4
Асинхронная работа с сетью и бд
доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
from sqlalchemy.ext.asyncio import AsyncSession, async_session

from homework_04.models import Base


def create_table:
    conn.run_sync(Base.metadata.drop_all)
    conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

async def save_posts():


async def async_main():
    pass


def main():
    pass


if __name__ == "__main__":
    main()