import os
import qdrant_client
from fastembed import TextEmbedding
from qdrant_client.http import models as rest
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Access the environment variables
QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

# Initialize Qdrant client
qdrant_client = qdrant_client.QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

collection_name = "book-collection"

# Check if the client is connected
try:
    collections = qdrant_client.get_collections()
    print("Connected to Qdrant")
    print(f"Available collections: {collections.collections}")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")

# Initialize the FastEmbed model
embedding_model = TextEmbedding()

# Verify the chosen Embedding model
print(f"Using embedding model: {embedding_model.model_name}")

# Function to generate embedding
def generate_embedding(query_text):
    try:
        embeddings = list(embedding_model.embed([query_text]))
        print(f"Generated embedding: {embeddings[0][:10]}...")  # Print the first 10 elements for verification
        return embeddings[0]
    except Exception as e:
        print(f"Failed to generate embedding: {e}")
        return None

# Function to create collection
def create_collection():
    try:
        qdrant_client.recreate_collection(
            collection_name=collection_name,
            vectors_config=rest.VectorParams(size=384, distance=rest.Distance.COSINE)
        )
        print(f"Collection '{collection_name}' is ready.")
    except Exception as e:
        print(f"Failed to create or verify collection: {e}")

# Function to insert data into collection
def insert_data():
    try:
        # Assuming data is loaded into `data_points` list with proper structure
        # Example structure: [{'id': 1, 'vector': [0.1, 0.2, ...], 'payload': {'title': 'Book Title', ...}}, ...]
        data_points = [
            {
                "id": 1,
                "vector": generate_embedding("rage of angels, sidney sheldon"),
                "payload": {"title": "Rage of Angels", "description": "A novel by Sidney Sheldon", "categories": ["Fiction"]}
            }
            # Add more data points as needed
        ]

        operations = [
            rest.PointStruct(id=point['id'], vector=point['vector'], payload=point['payload'])
            for point in data_points
        ]

        qdrant_client.upsert(collection_name=collection_name, points=operations)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Failed to insert data: {e}")

# Function to search in collection
def search_collection(query_text):
    query_vector = generate_embedding(query_text)
    if query_vector is not None:
        try:
            print(f"Query vector: {query_vector[:10]}...")  # Print the first 10 elements of the query vector
            search_result = qdrant_client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=4
            )

            if not search_result:
                print("No results found")
            else:
                for point in search_result:
                    title = point.payload.get('title', 'Unknown Title')
                    description = point.payload.get('description', 'No description available')
                    categories = point.payload.get('categories', 'Uncategorized')

                    print(f"Title: {title}\nDescription: {description}\nCategories: {categories}\n---")

        except Exception as e:
            print(f"Failed to perform search: {e}")
    else:
        print("Query vector is not available.")

# Step 1: Create or verify the collection
create_collection()

# Step 2: Insert data into the collection
insert_data()

# Step 3: Perform a search in the collection
search_collection("rage of angels, sidney sheldon")
