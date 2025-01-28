ARG PYTHON_VERSION_MAJOR="3"
ARG PYTHON_VERSION_MINOR="11"
ARG PYTHON_VERSION_PATCH="3"
ARG PYTHON_VERSION="${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}.${PYTHON_VERSION_PATCH}"

ARG UV_VERSION="0.5.24"

FROM python:${PYTHON_VERSION}-alpine3.18 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /home/nifcloud
COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


FROM python:${PYTHON_VERSION}-alpine3.18
ARG PYTHON_VERSION_MAJOR
ARG PYTHON_VERSION_MINOR
COPY --from=builder \
    /home/nifcloud/.venv/lib/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages \
    /usr/local/lib/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages

RUN apk --update add groff

RUN adduser -D nifcloud
USER nifcloud
WORKDIR /home/nifcloud

ENV PATH="/home/nifcloud/.local/bin:${PATH}"

COPY . .
COPY bin/nifcloud /usr/local/bin/nifcloud

ENTRYPOINT ["/usr/local/bin/nifcloud"]
