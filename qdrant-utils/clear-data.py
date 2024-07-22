import os
from qdrant_client import QdrantClient

# Initialize Qdrant client with provided credentials
qdrant_client = QdrantClient(
    url="https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
)

collection_name = "book-collection"

try:
    # Check if collection exists and delete if it does
    if qdrant_client.collection_exists(collection_name):
        qdrant_client.delete_collection(collection_name)
        print(f"Collection '{collection_name}' deleted successfully.")

    # Recreate the collection
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=1536,  # This should match the output size of your embedding model
            distance="Cosine"  # or "Dot" depending on your use case
        )
    )
    
    print(f"Collection '{collection_name}' created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
