import os
import csv
from concurrent.futures import ThreadPoolExecutor
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct
from fastembed import TextEmbedding
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access the environment variables
QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
CSV_FILE_PATH = '/mnt/c/Users/SUPERADMIN/OneDrive/POSO/book-hunt-engine/data/books.csv'
COLLECTION_NAME = 'book-lib'  # Set the new collection name

# Print out the environment variables to debug
print(f"QDRANT_URL: {QDRANT_URL}")
print(f"QDRANT_API_KEY: {QDRANT_API_KEY}")
print(f"CSV_FILE_PATH: {CSV_FILE_PATH}")

# Initialize Qdrant client
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# Initialize the FastEmbed model
embedding_model = TextEmbedding(model_name="BAAI/bge-base-en")

# Function to generate embedding
def generate_embedding(book_data):
    text = f"{book_data['title']} {book_data['description']}"
    embeddings = list(embedding_model.embed([text]))
    return embeddings[0]

# Function to prepare point data
def prepare_point(row):
    try:
        # Validate and convert data
        doc_id = int(row["isbn13"])
        average_rating = float(row["average_rating"]) if row["average_rating"] else None
        published_year = int(row["published_year"]) if row["published_year"] else None
        authors = row["authors"].split(", ") if row["authors"] else []

        vector = generate_embedding(row)
        payload = {
            "title": row["title"],
            "categories": row["categories"],
            "thumbnail": row["thumbnail"],
            "description": row["description"],
            "average_rating": average_rating,
            "published_year": published_year,
            "authors": authors
        }

        return PointStruct(
            id=doc_id,
            vector=vector,
            payload=payload
        )
    except (ValueError, KeyError) as e:
        # Skip rows with invalid data
        print(f"Skipping row due to error: {e}")
        return None

# Function to upsert points in batch
def upsert_points_batch(points_batch):
    valid_points = [point for point in points_batch if point is not None]
    if valid_points:
        qdrant_client.upsert(
            collection_name=COLLECTION_NAME,
            points=valid_points
        )

# Main function to process CSV and upsert data
def main():
    points_batch = []
    batch_size = 100  # Adjust the batch size as needed

    if CSV_FILE_PATH is None:
        print("CSV_FILE_PATH is not set. Exiting.")
        return

    if not os.path.isfile(CSV_FILE_PATH):
        print(f"CSV file does not exist at path: {CSV_FILE_PATH}")
        return

    with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust the number of workers as needed
            for row in reader:
                point = prepare_point(row)
                points_batch.append(point)

                if len(points_batch) >= batch_size:
                    executor.submit(upsert_points_batch, points_batch)
                    points_batch = []

            if points_batch:
                executor.submit(upsert_points_batch, points_batch)

if __name__ == "__main__":
    main()
    print("Data ingestion completed successfully.")
