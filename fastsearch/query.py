import os
from qdrant_client import QdrantClient
from fastembed import TextEmbedding
from dotenv import load_dotenv
from qdrant_client.http.models import Distance, VectorParams

# Load environment variables from a .env file
load_dotenv()

# Access the environment variables
QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')
COLLECTION_NAME = 'book-lib'

# Initialize Qdrant client
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

# Ensure the collection exists
def ensure_collection_exists():
    if not qdrant_client.collection_exists(COLLECTION_NAME):
        qdrant_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )

# Initialize the FastEmbed model
embedding_model = TextEmbedding(model_name="BAAI/bge-base-en")

# Function to generate query embedding
def generate_query_embedding(query_text):
    embeddings = list(embedding_model.embed([query_text]))
    return embeddings[0]

# Function to perform search
def search_books(query_text, limit=4):
    query_vector = generate_query_embedding(query_text)
    
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit
    )
    
    return search_result

# Ensure the collection exists when the script is imported
ensure_collection_exists()
