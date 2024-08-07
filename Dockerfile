FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry install --no-interaction --no-cache

COPY . /app/
