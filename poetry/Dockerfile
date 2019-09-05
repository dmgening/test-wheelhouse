FROM python:3.6 AS development

ENV PYTHONFAULTHANDLER=1 PYTHONUNBUFFERED=1 PYTHONHASHSEED=random \ 
    PIP_NO_CACHE_DIR=off PIP_DISABLE_PIP_VERSION_CHECK=on PIP_DEFAULT_TIMEOUT=100 \ 
    POETRY_VERSION=1.0.0b1

RUN pip install --quiet "poetry==$POETRY_VERSION"

WORKDIR /usr/src/app
COPY pyproject.toml poetry.lock /usr/src/app/
RUN poetry install --no-interaction --no-ansi && \
    poetry show --outdated --no-ansi && \
    poetry export --format requirements.txt --output requirements.txt && \
    pip wheel --wheel-dir dist/wheelhouse --requirement requirements.txt 

COPY . /usr/src/app
RUN poetry build --format wheel

FROM python:3.6-slim

COPY --from=development /usr/src/app/dist /tmp/app-dist
RUN pip install --no-index --find-links /tmp/app-dist/wheelhouse/ /tmp/app-dist/*.whl && \
    rm -rf /tmp/app-dist
