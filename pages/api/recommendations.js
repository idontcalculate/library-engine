import { Client } from '@qdrant/js-client-rest';
import dotenv from 'dotenv';
import FastEmbed from 'fastembed';

dotenv.config();

const client = new Client({
  apiKey: process.env.QDRANT_API_KEY,
  url: process.env.QDRANT_URL,
});

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', ['POST']);
    return res.status(405).end(`Method ${req.method} Not Allowed`);
  }

  const { bookTitle, category } = req.body;

  if (!bookTitle || !category) {
    return res.status(400).json({ error: 'Book title and category are required' });
  }

  try {
    const queryVector = await FastEmbed.embed([`${bookTitle} ${category}`]);
    
    const response = await client.search({
      collection_name: 'your_collection_name',
      vector: queryVector[0],
      top: 5, // number of recommendations to retrieve
    });

    const recommendations = response.result.map((result) => result.payload.title);

    return res.status(200).json({ recommendations });
  } catch (error) {
    console.error('Error querying Qdrant:', error);
    return res.status(500).json({ error: 'Internal Server Error' });
  }
}
