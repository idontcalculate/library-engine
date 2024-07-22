import os
import csv
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, PointStruct

# Initialize Qdrant client with provided credentials
qdrant_client = QdrantClient(
    url="https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.qdrant.io",
    api_key="J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
)

collection_name = "book-collection"

# Define vector parameters
vector_params = VectorParams(
    size=1536,  # This should match the output size of your embedding model
    distance="Cosine"  # or "Dot" depending on your use case
)

# Check if collection exists and delete if it does
try:
    existing_collections = qdrant_client.get_collections().collections
    if any(col.name == collection_name for col in existing_collections):
        qdrant_client.delete_collection(collection_name)

    # Create the collection
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=vector_params
    )

    print(f"Collection '{collection_name}' created successfully.")

    # Path to the CSV file
    csv_file_path = "/mnt/c/Users/SUPERADMIN/OneDrive/POSO/book-hunt-engine/data/books.csv"

    # Read and insert documents from CSV
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            doc_id = row["id"]
            vector = [float(val) for val in row["vector"].split(",")]  # Assuming 'vector' column contains comma-separated values
            payload = {
                "title": row["title"],
                "isbn10": row["isbn10"],
                "isbn13": row["isbn13"],
                "categories": row["categories"],
                "thumbnail": row["thumbnail"],
                "description": row["description"],
                "num_pages": int(row["num_pages"]),
                "average_rating": float(row["average_rating"]),
                "published_year": int(row["published_year"]),
                "authors": row["authors"].split(",")  # Assuming 'authors' column contains comma-separated values
            }

            qdrant_client.upsert(
                collection_name=collection_name,
                points=[
                    PointStruct(
                        id=doc_id,
                        vector=vector,
                        payload=payload
                    )
                ]
            )

    print("Documents added successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
