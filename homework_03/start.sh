#!/usr/bin/env bash

export $(grep -v '^#' .env | xargs)
uvicorn main.app:app --reload --port $APP_PORT --host $APP_HOST
