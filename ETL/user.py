import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['users']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    my_Date=datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days))
    document = {
        'email': random_email(),
        'passwordHash': random_string(10),
        'role': random_role(),
        'firstName': random_name(),
        'lastName': random_name(),
        'createdAt': my_Date
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the users collection.")