import os
import pymongo
from todo_app.data.item import Item

class DatabaseClient:
    def __init__(self):
        self.mongo_db_client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
        self.tasks = self.mongo_db_client[os.getenv("DATABASE_NAME")]['tasks']

    def get_tasks_from_db(self):
        return self.tasks.find()

    def update_task_status_in_db(self, task_id, new_status):
        findTaskQuery = {"_id" : task_id}
        newStatus = {"$set": {"status" : new_status}}
        self.tasks.update_one(findTaskQuery, newStatus)

    def add_task_to_db(self, task_name, task_description):
        newTask = { "name": task_name,
                "description": task_description,
                "status": "To Do" 
        }
        self.tasks.insert_one(newTask)

    def delete_item_in_db(self, task_id):
        findTaskQuery = {"_id" : task_id}
        self.tasks.delete_one(findTaskQuery)
    
    def get_items(self):
        database_results = self.get_tasks_from_db()
        if database_results == None:
            return []
        tasks_array = [
            Item.from_database_entry(task)
            for task in database_results
        ]
        tasks_array.sort(key=lambda x: x.get_status(), reverse=True)
        return tasks_array
    
    def update_task_status(self, card_id, card_status):
        updated_status = self.get_updated_status_string(card_status)
        self.update_task_status_in_db(card_id, updated_status)

    def get_updated_status_string(self, card_status):
        if (card_status == "To Do"):
            return "Started"
        if (card_status == "Started"):
            return "Done"
        if (card_status == "Done"):
            return "To Do"