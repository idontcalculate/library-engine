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
    qdrant_client.get_collections()
    print("Connected to Qdrant")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")

# Initialize the FastEmbed model
embedding_model = TextEmbedding()

# Verify the chosen Embedding model
print(f"Using embedding model: {embedding_model.model_name}")

# Function to generate embedding
def generate_embedding(query_text):
    try:
        # Convert the generator to a list and then access the first element
        return list(embedding_model.embed([query_text]))[0]
    except Exception as e:
        print(f"Failed to generate embedding: {e}")
        return None

# Generative Search
query_text = "technology, data structures and algorithms, distributed systems"
query_vector = generate_embedding(query_text)

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
