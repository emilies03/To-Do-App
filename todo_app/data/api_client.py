import os
import requests

def get_cards_request():
    result = requests.get(f'https://api.trello.com/1/boards/{os.getenv("BOARD_ID")}/lists?cards=open&key={os.getenv("SECRET_KEY")}&token={os.getenv("TOKEN")}')
    if (result.status_code == 200):
        return result.json()

def create_new_card(card_name):
    requests.post(f'https://api.trello.com/1/cards?name={card_name}&idList={os.getenv("TO_DO_LIST_ID")}&key={os.getenv("SECRET_KEY")}&token={os.getenv("TOKEN")}')
