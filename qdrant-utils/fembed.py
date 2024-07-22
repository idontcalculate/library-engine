import os
import qdrant_client
from qdrant_client.http import models as rest
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

# Initialize Qdrant client with the correct URL
qdrant_client = qdrant_client.QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

collection_name = "book-collection"

# Check if the client is connected
try:
    qdrant_client.get_collections()
    print("Connected to Qdrant")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")

# Initialize embedding model
from fastembed import TextEmbedding

embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
print(f"Using embedding model: {embedding_model.model_name}")

# Generative Search
query_text = "technology, data structures and algorithms, distributed systems"
try:
    query_vector = next(embedding_model.encode([query_text]))  # Encode query text to vector
except Exception as e:
    print(f"Failed to generate embedding: {e}")
    query_vector = None

if query_vector is not None:
    try:
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
