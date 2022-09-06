import os
from todo_app.data.api_client import get_cards_request, create_new_card, move_card_to_list
from todo_app.data.item import Item

def get_items():
    cards_result = get_cards_request()
    card_array = [
        Item.from_trello_card(card, list)
        for list in cards_result
        for card in list['cards']
    ]
    return card_array

def update_task_status(card_id, card_status):
    next_list_id = get_next_list_id(card_status)
    move_card_to_list(card_id, next_list_id)

def add_item(item_name):
    create_new_card(item_name)

def get_next_list_id(card_status):
    match card_status:
        case "To Do":
            return os.getenv("STARTED_LIST_ID")
        case "Started":
            return os.getenv("DONE_LIST_ID")
        case "Done":
            return os.getenv("TO_DO_LIST_ID")
