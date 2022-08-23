import os
from flask import session
from todo_app.data.api_client import get_cards_request, create_new_card, move_card_to_list
from todo_app.data.card import Card

def get_items():
    cards_result = get_cards_request()
    card_array = []
    for list in cards_result:
            for card in list["cards"]:
                card_array.append(
                    Card.from_trello_card(card, list)
                )
    return card_array

def update_task_status(card_id, card_status):
    next_list_id = get_next_list_id(card_status)
    move_card_to_list(card_id, next_list_id)

def add_item(card_name):
    create_new_card(card_name)

def get_next_list_id(card_status):
    match card_status:
        case "To Do":
            return os.getenv("STARTED_LIST_ID")
        case "Started":
            return os.getenv("DONE_LIST_ID")
        case "Done":
            return os.getenv("TO_DO_LIST_ID")
