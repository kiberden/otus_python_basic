"""Главный модуль."""
import json
from fastapi import FastAPI, Response


route = FastAPI()


@route.get('/ping/')
async def ping() -> Response:
    """Обработать запросы к серверу."""
    return Response(
        content=json.dumps({'message': 'pong'}),
        media_type='application/json',
    )
