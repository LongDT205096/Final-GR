import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Movie {
    title: string;
    year: number;
    ave_rating: number;
    genres: string[];
    directors: string[];
    actors: string[];
    image_url: string;
    duration: number;
    description: string;
    summary: string;
    storyline: string;
}

const App: React.FC = () => {
    const [movies, setMovies] = useState<Movie[]>([]);

    useEffect(() => {
        const fetchMovies = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/movies/all/');
                setMovies(response.data);
            } catch (error) {
                console.error('Error fetching movies:', error);
            }
        };
        fetchMovies();
    }, []);

    return (
        <div>
            <h1>Movies</h1>
            <ul>
                {movies.map((movie, index) => (
                    <li key={index}>
                        <h2>{movie.title}</h2>
                        <p>Year: {movie.year}</p>
                        <p>Average Rating: {movie.ave_rating}</p>
                        <p>Genres: {movie.genres.join(', ')}</p>
                        <p>Directors: {movie.directors.join(', ')}</p>
                        <p>Actors: {movie.actors.join(', ')}</p>
                        <p>Image URL: {movie.image_url}</p>
                        <p>Duration: {movie.duration}</p>
                        <p>Description: {movie.description}</p>
                        <p>Summary: {movie.summary}</p>
                        <p>Storyline: {movie.storyline}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;
