FROM python:3.11

WORKDIR /workspace

COPY main.py .
COPY poetry.lock .
COPY pyproject.toml .

RUN pip install --upgrade pip poetry && \
    poetry install --no-root

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]
