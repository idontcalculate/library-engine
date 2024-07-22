from qdrant_client import QdrantClient
import requests

# Set up the Qdrant client with your credentials
qdrant_client = QdrantClient(
    url="https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.cloud.qdrant.io",
    api_key="J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
)

# Check the status of the Qdrant service
try:
    response = requests.get("https://edf45dc6-1789-46c0-aef0-4d96fc18ee1d.us-east4-0.gcp.cloud.qdrant.io/collections", headers={
        "api-key": "J2tDEiNuzJ_AQavako7PB4QY7Eao9WTsS-hpPaxT8lj7G-vW4FhRMw"
    })
    response.raise_for_status()
    print("Connection successful. Collections:", response.json())
except requests.exceptions.RequestException as e:
    print("Failed to connect to Qdrant:", e)
