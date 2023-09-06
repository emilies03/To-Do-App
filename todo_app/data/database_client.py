import os
import pymongo
from todo_app.data.item import Item
from todo_app.data.logging import logInfo, logError

class DatabaseClient:
    def __init__(self):
        try:
            self.mongo_db_client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
            self.tasks = self.mongo_db_client[os.getenv("DATABASE_NAME")]['tasks']
        except Exception as e:
            logError(f'Unable to connect to DB, error: {e}')
            

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
            logInfo(f'No tasks in database')
            return []
        tasks_array = [
            Item.from_database_entry(task)
            for task in database_results
        ]
        logInfo(f'{len(tasks_array)} tasks returned from database')
        tasks_array.sort(key=lambda x: x.get_status(), reverse=True)
        return tasks_array
    
    def update_task_status(self, task_id, task_status):
        updated_status = self.get_updated_status_string(task_status)
        self.update_task_status_in_db(task_id, updated_status)

    def get_updated_status_string(self, task_status):
        new_status = "To Do"
        if (task_status == "To Do"):
            new_status = "Started"
        if (task_status == "Started"):
            new_status = "Done"
        logInfo(f'Updating status from {task_status} to {new_status}')
        return new_status