from todo_app.data.api_client import create_new_card, move_card_to_list
from todo_app.data.item import Item
from todo_app.data.database_client import get_tasks_from_db, update_task_status_in_db

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
    updated_status = get_updated_status_string(card_status)
    update_task_status_in_db(card_id, updated_status)

def add_item(item_name):
    create_new_card(item_name)

def get_updated_status_string(card_status):
    if (card_status == "To Do"):
        return "Started"
    if (card_status == "Started"):
        return "Done"
    if (card_status == "Done"):
        return "To Do"
