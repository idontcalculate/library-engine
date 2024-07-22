import os
import qdrant_client
import openai
from qdrant_client.http import models as rest
from dotenv import load_dotenv

load_dotenv()

QDRANT_HOST = os.getenv('QDRANT_HOST') 
QDRANT_PORT = os.getenv('QDRANT_PORT') or 6333
QDRANT_API_KEY = os.getenv('QDRANT_API_KEY') 
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

qdrant_client = qdrant_client.QdrantClient(
    url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
    api_key=QDRANT_API_KEY
)

collection_name = "book-collection"

# Check if the client is connected
try:
    qdrant_client.get_collections()
    print("Connected to Qdrant")
except Exception as e:
    print(f"Failed to connect to Qdrant: {e}")

# Generative Search
query_text = "technology, data structures and algorithms, distributed systems"
query_vector = [0.0] * 300  # Placeholder for the actual query vector

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

            prompt = (f"Explain why this book might be interesting to someone who likes playing the violin, rock climbing, "
                      f"and doing yoga. The book's title is {title}, with a description: {description}, and is in the genre: {categories}.")

            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=150
            )

            generated_text = response.choices[0].text.strip()
            print(f"Title: {title}\nDescription: {description}\nCategories: {categories}\nGenerated: {generated_text}\n---")

except Exception as e:
    print(f"Failed to perform search: {e}")
