import pytest
import os
import requests
from dotenv import load_dotenv, find_dotenv
from todo_app import app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', get_lists_stub)
    response = client.get('/')

    assert response.status_code == 200
    assert "Test card" in response.data.decode()

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

    def raise_for_status(self):
        return    

def get_lists_stub(url):
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?cards=open&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}':
        fake_response_data = [{
            'id': '123abc',
            'name': 'To Do',
            'cards': [{'id': '456', 'name': 'Test card', 'desc': 'task description'}]
        }]
    return StubResponse(fake_response_data)
