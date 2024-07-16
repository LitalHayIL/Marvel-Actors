import React, { useState } from 'react';
import axios from 'axios';
import Spinner from './components/Spinner';
import './App.css';

function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [movies, setMovies] = useState({});
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    try {
      setLoading(true);

      const moviesResponse = await axios.get(`http://localhost:5000/moviesPerActor?actorName=${searchTerm}`);
      setMovies(moviesResponse.data);

    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1 className="title">Welcome to the Marvel actors search</h1>
      <div className="search-container">
        <input
          type="text"
          placeholder="Search for an actor"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
        <button onClick={handleSearch} className="search-button">Search</button>
      </div>

      {loading ? (
        <Spinner />
      ) : (
        <>
          <h2>Movies per Actor</h2>
          {Object.entries(movies).map(([actorName, movieDetails]) => (
            <div key={actorName}>
              <h3>{actorName}</h3>
              <ul className="movie-list">
                {movieDetails.map(({ title, character, year }) => (
                  <li key={title} className="movie-item">
                    {title} ({year}) - {character}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </>
      )}
    </div>
  );
}

export default App;