import os
import pymongo

def get_tasks_from_db():
    tasksCollection = get_tasks_collection_from_db()
    return tasksCollection.find()

def update_task_status_in_db(task_id, new_status):
    tasksCollection = get_tasks_collection_from_db()
    findTaskQuery = {"_id" : task_id}
    newStatus = {"$set": {"status" : new_status}}
    tasksCollection.update_one(findTaskQuery, newStatus)

def add_task_to_db(task_name):
    tasksCollection = get_tasks_collection_from_db()
    newTask = { "name": task_name,
               "description": "",
               "status": "To Do" 
    }
    tasksCollection.insert_one(newTask)


def get_tasks_collection_from_db():
    client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
    return client[os.getenv("DATABASE_NAME")]['tasks']