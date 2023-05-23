"""Модуль приложения."""
import os

import uvicorn
from fastapi import APIRouter, FastAPI

from main import api


def init_app() -> FastAPI:
    """Инициализация приложения."""
    app = FastAPI()
    main_router = APIRouter()
    main_router.include_router(api.router)
    app.include_router(main_router)
    return app


app = init_app()


if __name__ == "__main__":
    uvicorn.run(
        app, host=os.getenv('APP_HOST'), port=os.getenv('APP_PORT'), reload=True
    )
