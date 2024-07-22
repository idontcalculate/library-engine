from fastembed.embedding import TextEmbedding

def get_book_vector(book_data):
    embedder = TextEmbedding(model_name="BAAI/bge-base-en")
    text = f"{book_data['title']} {book_data['description']}"
    vector = list(embedder.embed(text))
    return vector[0]  # Since embed returns a generator, we convert it to a list and take the first item.

def get_query_vector(query_text):
    embedder = TextEmbedding(model_name="BAAI/bge-base-en")
    vector = list(embedder.embed(query_text))
    return vector[0] # same as the upper one
