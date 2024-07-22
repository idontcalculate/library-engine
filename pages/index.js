import { useState } from 'react';

export default function Home() {
  const [bookTitle, setBookTitle] = useState('');
  const [category, setCategory] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const getRecommendations = async () => {
    try {
      const response = await fetch('/api/recommendations', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ bookTitle, category }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setRecommendations(data.recommendations || []);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
      setRecommendations([]);
    }
  };

  return (
    <div>
      <h1>Book Hunt Engine</h1>
      <label>
        Book Title:
        <input
          type="text"
          value={bookTitle}
          onChange={(e) => setBookTitle(e.target.value)}
        />
      </label>
      <label>
        Category:
        <input
          type="text"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />
      </label>
      <button onClick={getRecommendations}>Get Recommendations</button>
      {recommendations.length > 0 ? (
        <ul>
          {recommendations.map((rec, index) => (
            <li key={index}>{rec}</li>
          ))}
        </ul>
      ) : (
        <p>No recommendations found for your query.</p>
      )}
      <footer>
        Made with ❤️ by <a href="https://github.com/idontcalculate">@idontcalculate</a> and built with <a href="https://qdrant.tech">Qdrant</a>.
      </footer>
    </div>
  );
}
