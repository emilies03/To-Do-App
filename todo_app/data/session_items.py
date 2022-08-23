from flask import session
from todo_app.data.api_client import get_cards_request, create_new_card
from todo_app.data.card import Card

def get_items():
    cards_result = get_cards_request()
    card_array = []
    for list in cards_result:
            for card in list["cards"]:
                card_array.append(
                    Card(card["id"], card["name"], list["name"], card["desc"])
                )
    return card_array

def update_task_status(id):
    item = get_item(id)
    if (item["status"] == "Not Started"):
        item["status"] = "Complete"
    else:
        item["status"] = "Not Started"
    save_item(item)

def get_item(id):
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)

def add_item(card_name):
    create_new_card(card_name)

def save_item(item):
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]
    session['items'] = updated_items

    return item
