import { TextEmbedding } from 'fastembed';

export const getQueryVector = async (query) => {
    const embedder = new TextEmbedding();
    const embedding = await embedder.generate(query_text);
    return embedding[0].vector;  // Adjust to match your embedding structure
};
