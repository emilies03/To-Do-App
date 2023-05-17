import os
import requests

def create_new_card(card_name):
    requests.post(f'https://api.trello.com/1/cards?name={card_name}&idList={os.getenv("TO_DO_LIST_ID")}&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}')

def move_card_to_list(card_id, list_id):
    requests.put(f'https://api.trello.com/1/cards/{card_id}?idList={list_id}&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}')