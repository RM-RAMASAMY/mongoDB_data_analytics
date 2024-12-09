from pprint import pprint
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
from pymongo import MongoClient

# Connect to MongoDB
source_client = MongoClient("mongodb://localhost:27017/")
target_client = MongoClient("mongodb://localhost:27017/")

# Source and target database and collection details
source_db = source_client["source"]
source_collection = source_db["comment"]

target_db = target_client["target"]
target_collection = target_db["comment"]

# Fetch documents using the cursor
cursor = source_collection.find()

# Flatten each document in the cursor
flattened_docs = [flatten_dict(doc) for doc in cursor]

# Example output
pprint(flattened_docs[0])

try:
    # Insert transformed documents into the target collection
    target_collection.insert_many(flattened_docs)
    print(f"Copied and transformed {source_collection.count_documents({})} documents.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connections
    source_client.close()
    target_client.close()