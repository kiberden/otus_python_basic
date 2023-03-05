"""Модуль API проекта."""
import json

from fastapi_utils.inferring_router import InferringRouter
from fastapi import Response

router = InferringRouter()


@router.get("/ping/")
async def ping() -> Response:
    """Обработать запросы к серверу."""
    return Response(
        content=json.dumps({"message": "pong"}),
        media_type="application/json",
    )
