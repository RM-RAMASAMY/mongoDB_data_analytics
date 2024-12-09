from pymongo import MongoClient, UpdateOne
from collections import defaultdict
from datetime import datetime

# Connect to MongoDB
source_client = MongoClient("mongodb://localhost:27017/")
target_client = MongoClient("mongodb://localhost:27017/")

# Source and target database and collection details
source_db = source_client["source"]
source_collection = source_db["applicants"]

target_db = target_client["target"]
target_collection = target_db["applicant_Signups"]

# Fetch documents using the cursor
cursor = source_collection.find()

# Group documents by month
monthly_summary = defaultdict(list)

for doc in cursor:
    created_at = doc.get('createdAt')
    if created_at:
        month = created_at.strftime("%Y-%m")
        monthly_summary[month].append(doc)

# Summarize the grouped documents
summary = {month: len(docs) for month, docs in monthly_summary.items()}

target_collection.bulk_write([UpdateOne({"month": month}, {"$set": {"count": count}}, upsert=True) for month, count in summary.items()])
