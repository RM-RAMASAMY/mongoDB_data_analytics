import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from assets import *

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['source']
collection = db['applicants']

# Generate 100 documents based on the schema
documents = []
for _ in range(100):
    document = {
        'name': random_name(),
        'userId': random_objectid(),
        'resume': random_string(50),
        'phone': random_phone(),
        'address': random_address(),
        'skills': random_skills(),
        'appliedJobs': [random_objectid() for _ in range(random.randint(0, 3))],
        'createdAt': datetime(2022, 1, 1) + timedelta(days=random.randint(0, (datetime.now() - datetime(2022, 1, 1)).days)),
        'followingCompanies': [random_company_id() for _ in range(random.randint(0, 3))],
        'followingApplicants': [random_objectid() for _ in range(random.randint(0, 3))]
    }
    documents.append(document)

# Insert documents into the collection
collection.insert_many(documents)

print("Inserted 100 documents into the applicants collection.")