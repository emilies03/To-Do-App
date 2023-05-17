import os
from todo_app.data.api_client import create_new_card, move_card_to_list
from todo_app.data.item import Item
from todo_app.data.database_client import get_tasks_from_db

def get_items():
    database_results = get_tasks_from_db()
    if database_results == None:
        return []
    tasks_array = [
        Item.from_database_entry(task)
        for task in database_results
    ]
    return tasks_array

def update_task_status(card_id, card_status):
    next_list_id = get_next_list_id(card_status)
    move_card_to_list(card_id, next_list_id)

def add_item(item_name):
    create_new_card(item_name)

def get_next_list_id(card_status):
    if (card_status == "To Do"):
        return os.getenv("STARTED_LIST_ID")
    if (card_status == "Started"):
        return os.getenv("DONE_LIST_ID")
    if (card_status == "Done"):
        return os.getenv("TO_DO_LIST_ID")
