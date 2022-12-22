FROM python:3.10.4-slim-buster as base
RUN pip install poetry
WORKDIR /app
COPY poetry.lock poetry.toml pyproject.toml /app/
RUN poetry install

FROM base as production
EXPOSE 8000 
COPY . /app/
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as developer
EXPOSE 5000 
ENTRYPOINT poetry run flask run -h 0.0.0.0