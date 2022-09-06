import os
import requests

def get_cards_request():
    result = requests.get(f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?cards=open&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}')
    result.raise_for_status() 
    return result.json()

def create_new_card(card_name):
    requests.post(f'https://api.trello.com/1/cards?name={card_name}&idList={os.getenv("TO_DO_LIST_ID")}&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}')

def move_card_to_list(card_id, list_id):
    requests.put(f'https://api.trello.com/1/cards/{card_id}?idList={list_id}&key={os.getenv("API_KEY")}&token={os.getenv("TOKEN")}')