# Marvel-Actors

This project is a web application that allows users to search for Marvel actors. It provides information about the movies each actor has played in, actors who have played multiple Marvel characters, and characters that have been portrayed by multiple actors.

## Features

- Search for movies per actor
- Display actors who have played multiple Marvel characters
- Show characters that have been portrayed by multiple actors

## Technologies Used

- Frontend: React
- Backend: Python (Flask)
- API: The Movie Database (TMDb) API

## Prerequisites

Before running the project, ensure you have the following installed:

- Node.js
- Python 3
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone git@github.com:LitalHayIL/marvel-actors.git
   ```

2. Navigate to the project directory:
   ```
   cd marvel-actors
   ```

3. Install the frontend dependencies:
   ```
   cd frontend
   npm install
   ```

4. Install the backend dependencies:
   ```
   cd ../backend
   pip install -r requirements.txt
   ```

## Configuration

1. Obtain an API key from The Movie Database (TMDb) by creating an account at [https://www.themoviedb.org/](https://www.themoviedb.org/).

2. In the `backend` directory, create a `.env` file and add your TMDb API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

1. Start the backend server:
   ```
   cd backend
   python app.py
   ```

2. In a new terminal window, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your web browser and navigate to `http://localhost:3000` to access the application.

4. Use the search input to enter an actor's name and click the "Search" button to fetch movies for that actor.

## API Endpoints

- `/moviesPerActor`: Retrieves movies per actor.
- `/actorsWithMultipleCharacters`: Retrieves actors who have played multiple Marvel characters.
- `/charactersWithMultipleActors`: Retrieves characters that have been portrayed by multiple actors.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [The Movie Database (TMDb)](https://www.themoviedb.org/) for providing the movie data API.
- [React](https://reactjs.org/) for the frontend framework.
- [Flask](https://flask.palletsprojects.com/) for the backend framework.
```