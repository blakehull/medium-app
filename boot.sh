#!/bin/sh

PORT=${PORT:-8080}
HOST=${HOST:-0.0.0.0}

echo "Starting app on host ${HOST}, port ${PORT}"
uvicorn core.controller:app --host ${HOST} --port ${PORT} --reload