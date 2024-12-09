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
source_collection = source_db["jobs"]

target_db = target_client["target"]
target_collection = target_db["jobs"]

# Fetch documents using the cursor
cursor = source_collection.find()

# Flatten each document in the cursor
flattened_docs = [flatten_dict(doc) for doc in cursor]

def transform_document(flat_doc):
    # Example transformation: Add a new field and modify an existing field
    requirements = [requirement.lower() for requirement in flat_doc.get('requirements', [])]
    flat_doc["Python"] = 1 if 'python' in requirements else 0
    flat_doc["Java"] = 1 if 'java' in requirements else 0
    flat_doc["C++"] = 1 if 'c++' in requirements else 0
    flat_doc["JavaScript"] = 1 if 'javascript' in requirements else 0
    flat_doc["SQL"] = 1 if 'sql' in requirements else 0
    flat_doc["HTML"] = 1 if 'html' in requirements else 0
    flat_doc["CSS"] = 1 if 'css' in requirements else 0
    flat_doc["React"] = 1 if 'react' in requirements else 0
    flat_doc["Node.js"] = 1 if 'node.js' in requirements else 0
    flat_doc["Django"] = 1 if 'django' in requirements else 0
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