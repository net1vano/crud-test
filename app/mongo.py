from pymongo import MongoClient
import os

mongo_host = os.getenv("MONGO_HOST", "127.0.0.1")
mongo_port = int(os.getenv("MONGO_PORT", 27017))
client = MongoClient(mongo_host, mongo_port)
db = client.cruddata  # выбор базы
data = db.data  # выбор коллекции