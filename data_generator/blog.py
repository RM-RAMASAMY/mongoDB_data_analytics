import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['blog']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    author_type = random_role()
    my_Date=datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days))
    document = {
        'title': random_string(15),
        'content': random_string(100),
        'authorType': author_type,
        'authorId': random_objectid(),
        'tags': random_tags(),
        'createdAt': my_Date,
        'updatedAt': my_Date + timedelta(days=random.randint(0, 10)),
        'likesCount': random.randint(0, 100),
        'commentsCount': random.randint(0, 50)
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the blogs collection.")