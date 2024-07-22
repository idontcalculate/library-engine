import os
import numpy as np
from qdrant_client import QdrantClient
from fastembed.embedding import TextEmbedding
from qdrant_client.http.models import VectorParams, Distance
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

QDRANT_URL = os.getenv('QDRANT_URL') 
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

# Initialize FastEmbed model
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Verify the chosen Embedding model
print(f"Using embedding model: {embedding_model.model_name}")

# Initialize Qdrant client
qdrant_client = QdrantClient(
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

# Ensure the collection exists with the correct vector size
try:
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print(f"Collection '{collection_name}' is ready.")
except Exception as e:
    print(f"Failed to create or update collection: {e}")

# Define the query text and generate the embedding
query_text = "technology, data structures and algorithms, distributed systems"
try:
    query_vector = np.array(embedding_model.embed([query_text])[0])
    print(f"Query Vector: {query_vector}")

    # Perform the search
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

except Exception as e:
    print(f"Failed to generate embedding: {e}")