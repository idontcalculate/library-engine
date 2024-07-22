import os
import json
import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from fastembed import TextEmbedding
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

# Initialize FastEmbed model
embedding_model = TextEmbedding()

# Verify the chosen Embedding model
print("The model BAAI/bge-small-en-v1.5 is ready to use.")

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

# Define the query text and generate the embedding
query_text = "technology, data structures and algorithms, distributed systems"
try:
    query_vector = np.array(list(embedding_model.embed([query_text]))[0])

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
