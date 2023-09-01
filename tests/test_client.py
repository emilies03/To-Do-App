import pytest
import mongomock
import pymongo
import os
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    databaseClient = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
    tasks = databaseClient[os.getenv("DATABASE_NAME")]['tasks']
    tasks.insert_one({
        "name": "task_name",
        "description": "task_description",
        "status": "To Do" 
    })
    response = client.get('/')

    assert response.status_code == 200
    assert "task_name" in response.data.decode()