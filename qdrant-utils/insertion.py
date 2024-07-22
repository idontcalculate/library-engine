import os
import csv
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, PointStruct
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access the environment variables
QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

# Initialize Qdrant client with provided credentials
qdrant_client = QdrantClient(
    url="https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
)

collection_name = "book-collection"

try:
    # Read and insert documents from CSV
    csv_file_path = "/mnt/c/Users/SUPERADMIN/OneDrive/POSO/book-hunt-engine/data/books.csv"

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        headers = reader.fieldnames
        print(f"CSV Headers: {headers}")  # Debug print to verify headers once
        
        for row in reader:
            try:
                doc_id = int(row["id"])  # Assuming 'id' column is in the CSV
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

                # Check if the document ID already exists
                existing_point = qdrant_client.get_point(collection_name, doc_id)
                if existing_point:
                    print(f"Document with ID {doc_id} already exists. Skipping.")
                else:
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
            except KeyError as e:
                # Redirect error to log file instead of printing to console
                with open('error_log.txt', 'a') as log_file:
                    log_file.write(f"Missing column in row: {e}, row data: {row}\n")

    print("Documents added successfully.")

except Exception as e:
    print(f"An error occurred: {e}")