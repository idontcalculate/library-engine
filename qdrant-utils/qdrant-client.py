from qdrant_client import QdrantClient

# Initialize Qdrant client with provided credentials
qdrant_client = QdrantClient(
    url="https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
)

try:
    collections = qdrant_client.get_collections()
    print("Connected to Qdrant")
    print("Collections:", collections)
except Exception as e:
    print(f"An error occurred: {e}")
