"""
Модуль получения данных из удаленного источника.
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp).
"""

import asyncio

from aiohttp import ClientSession

USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_json(url: str) -> dict:
    """ Запрос на получение данных по передаваемой ссылке. """
    async with ClientSession() as client:
        async with client.get(url) as response:
            return await response.json()


async def get_users():
    """ Получение пользователей. """
    return await fetch_json(USERS_DATA_URL)


async def get_posts():
    """ Получение постов. """
    return await fetch_json(POSTS_DATA_URL)


async def main():
    """ Главный метод. Запрашиваем все данные. """
    await get_users()
    await get_posts()


if __name__ == "__main__":
    asyncio.run(main())
