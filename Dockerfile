FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS build

ENV PYTHONUNBUFFERED=1
ENV UV_COMPILE_BYTE=1
ENV UV_LINK_MODE=copy
ENV UV_TOOL_BIN_DIR=/usr/local/bin
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock* /app/

# Устанавливаем зависимости без установки проекта
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-install-project --no-dev

# Копируем код проекта
COPY ./app /app/app
COPY ./app/settings /app/app/settings
COPY ./app/core /app/app/core
COPY ./app/infrastructure /app/app/infrastructure
COPY ./app/pipeline /app/app/pipeline
COPY ./app/api /app/app/api

# Финальная установка проекта
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

FROM python:3.13-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV HOME=/home/app
ENV PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN addgroup --system --gid 1000 app && adduser --system --uid 1000 --home /home/app app

WORKDIR /app

# Копируем виртуальное окружение
COPY --from=build --chown=app:app /app/.venv /app/.venv

# Копируем pyproject.toml (для метаданных)
COPY --from=build --chown=app:app /app/pyproject.toml /app/

# Копируем код приложения
COPY --from=build --chown=app:app /app/app /app/app

EXPOSE 8082

USER app

# Запуск FastAPI приложения (измените "app.main:app" под вашу структуру)
ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8082"]

# Healthcheck (создайте эндпоинт /health в вашем FastAPI приложении)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8082/health || exit 1