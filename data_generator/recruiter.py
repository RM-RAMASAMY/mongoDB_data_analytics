import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['recruiters']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    my_Date=datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days))
    document = {
        'userId': random_objectid(),
        'companyId': random_company_id(),
        'createdAt': my_Date
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the recruiters collection.")