FROM python3.12-alpine:3.20

ENV PYTHONPATH=/src

COPY app /src/app

COPY ["./pyproject.toml", ".env", "/src/"]

RUN ["poetry", "run", "python", "manage.py", "runserver"]