import os
import requests
import pymongo
import pprint

def get_tasks_from_db():
    client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
    tasksCollection = client[os.getenv("DATABASE_NAME")]['tasks']
    return tasksCollection.find()

def update_task_status_in_db(task_id, new_status):
    client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
    tasksCollection = client[os.getenv("DATABASE_NAME")]['tasks']
    findTaskQuery = {"_id" : task_id}
    newStatus = {"$set": {"status" : new_status}}
    tasksCollection.update_one(findTaskQuery, newStatus)