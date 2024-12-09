import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['jobs']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    my_Date=datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days))
    document = {
        'companyId': random_company_id(),
        'postedBy': random_company_name(),
        'title': random_title(),
        'description': random_string(100),
        'requirements': random_skills(),
        'location': randon_state(),
        'salary': random_salary(),
        'department': random_dept(),
        'type': random.choice(['Full-time', 'Part-time', 'Contract']),
        'status': random.choice(['Active', 'Closed']),
        'applicationsCount': random.randint(0, 100),
        'jobLink': random_url(),
        'createdAt': my_Date,
        'updatedAt': my_Date + timedelta(days=random.randint(0, (datetime.now() - my_Date).days))
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the jobs collection.")