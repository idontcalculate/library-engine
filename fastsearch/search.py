# search.py
import os
from fastembed import TextEmbedding
from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from dotenv import load_dotenv

load_dotenv()

QDRANT_URL = os.getenv('QDRANT_URL')
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY')

collection_name = COLLECTION_NAME

qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY
)

embedding_model = TextEmbedding()

def search_books(query_text, limit=4):
    try:
        query_vector = list(embedding_model.embed([query_text]))[0]
        search_result = qdrant_client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=limit
        )
        return search_result
    except Exception as e:
        print(f"Failed to perform search: {e}")
        return []

