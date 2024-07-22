import os
import qdrant_client
from qdrant_client.http import models as rest
from dotenv import load_dotenv
from fastembed import TextEmbedding

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

# Initialize embedding model
embedding_model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Check if the client is connected
try:
    collections = qdrant_client.get_collections()
    print("Connected to Qdrant")
    print(f"Available collections: {collections.collections}")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")

# Define collection name
collection_name = "book-collection"

# Define query text
query_text = "Murder in Mesopotamia, Agatha Christie, Detective and mystery"

# Generate embedding for the query text
try:
    query_embedding = list(embedding_model.embed(query_text))[0]  # Convert generator to list and get the first item
    print(f"Generated embedding: {query_embedding[:10]}...")
except Exception as e:
    print(f"Failed to generate embedding: {e}")
    query_embedding = None

if query_embedding:
    # Perform the search
    try:
        search_result = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=3
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
