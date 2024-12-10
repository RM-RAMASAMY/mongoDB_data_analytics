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


target_client.close()