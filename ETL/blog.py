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
source_collection = source_db["blog"]

target_db = target_client["target"]
target_collection = target_db["blog"]

# Fetch documents using the cursor
cursor = source_collection.find()

# Flatten each document in the cursor
flattened_docs = [flatten_dict(doc) for doc in cursor]

def transform_document(flat_doc):
    # Example transformation: Add a new field and modify an existing field
    tags = flat_doc.get('tags', [])
    flat_doc["AI"] = 1 if 'AI' in tags else 0
    flat_doc["Machine Learning"] = 1 if 'Machine Learning' in tags else 0
    flat_doc["Blockchain"] = 1 if 'Blockchain' in tags else 0
    flat_doc["Cloud Computing"] = 1 if 'Cloud Computing' in tags else 0
    flat_doc["DevOps"] = 1 if 'DevOps' in tags else 0
    flat_doc["Big Data"] = 1 if 'Big Data' in tags else 0
    flat_doc["Cybersecurity"] = 1 if 'Cybersecurity' in tags else 0
    flat_doc["IoT"] = 1 if 'IoT' in tags else 0
    flat_doc["5G"] = 1 if '5G' in tags else 0
    flat_doc["Quantum Computing"] = 1 if 'Quantum Computing' in tags else 0
    return flat_doc

# Process documents from the cursor
transformed_docs = [
    transform_document(doc) for doc in flattened_docs
]

# Example output
pprint(flattened_docs[0])

try:
    # Insert transformed documents into the target collection
    target_collection.insert_many(transformed_docs)
    print(f"Copied and transformed {source_collection.count_documents({})} documents.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connections
    source_client.close()
    target_client.close()