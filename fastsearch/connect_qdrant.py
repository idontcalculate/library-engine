from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from config import QDRANT_API_KEY, QDRANT_URL

def get_qdrant_client():
    qdrant_client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
    # Ensure the collection exists
    collection_name = "library"
    if not qdrant_client.collection_exists(collection_name):
        qdrant_client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )
    return qdrant_client