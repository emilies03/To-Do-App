import os
import requests
import pymongo
import pprint

def get_tasks_from_db():
    client = pymongo.MongoClient(os.getenv("PRIMARY_DB_CONNECTION_STRING"))
    tasksCollection = client[os.getenv("DATABASE_NAME")]['tasks']
    return tasksCollection.find()
