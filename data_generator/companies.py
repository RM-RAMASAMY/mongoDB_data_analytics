import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['companies']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    my_Date=datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days))
    document = {
        'name': random_company_name(),
        'description': random_string(50),
        'industry': random_ind(),
        'location': randon_state(),
        'followers': random.randint(0, 1000),
        'createdAt': my_Date,
        'website': f"https://{random_string(10)}.com"
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the companies collection.")