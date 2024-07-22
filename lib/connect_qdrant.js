import { QdrantClient } from '@qdrant/js-client-rest';
import dotenv from 'dotenv';

dotenv.config();

export const getQdrantClient = () => {
  return new QdrantClient({ apiKey: process.env.QDRANT_API_KEY });
};
