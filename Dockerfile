FROM python:3.10.4-slim-buster as base
RUN pip install poetry
WORKDIR /app
COPY . /app/
RUN poetry install
EXPOSE 8000 
ENTRYPOINT poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"