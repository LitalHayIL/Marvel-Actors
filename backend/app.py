from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


API_KEY = 'ac505a02032a33d65dd28b41f72182e1'
TMDB_BASE_URL = 'https://api.themoviedb.org/3'

@app.route('/')

def index():
    return jsonify({"message": "Welcome to the Marvel API"}), 200

@app.route('/moviesPerActor', methods=['GET'])
def movies_per_actor():
    actor_name = request.args.get('actorName')
    if not actor_name:
        return jsonify({"error": "Please provide an actor name"}), 400
    response = requests.get(f'{TMDB_BASE_URL}/search/person', params={
        'api_key': API_KEY,
        'query': actor_name
    })
    actor_data = response.json()
    if not actor_data['results']:
        return jsonify({"error": "Actor not found"}), 404
    actor_id = actor_data['results'][0]['id']
    response = requests.get(f'{TMDB_BASE_URL}/person/{actor_id}/movie_credits', params={
        'api_key': API_KEY
    })
    movies = response.json()['cast']


    movies_with_details = []
    for movie in movies:
        movie_id = movie['id']
        movie_title = movie['title']
        release_year = movie['release_date'][:4] if movie['release_date'] else 'N/A'
        
        response = requests.get(f'{TMDB_BASE_URL}/movie/{movie_id}/credits', params={
            'api_key': API_KEY
        })
        credits = response.json()['cast']
        character_name = next((credit['character'] for credit in credits if credit['name'] == actor_name), 'N/A')
        
        movies_with_details.append({
            'title': movie_title,
            'character': character_name,
            'year': release_year
        })
    
    return jsonify({actor_name: movies_with_details})

@app.route('/actorsWithMultipleCharacters', methods=['GET'])

def actors_with_multiple_characters():
    response = requests.get(f'{TMDB_BASE_URL}/person/popular', params={
        'api_key': API_KEY
    })
    popular_actors = response.json()['results']
    actors_roles = {}
    for actor in popular_actors:
        actor_id = actor['id']
        actor_name = actor['name']
        response = requests.get(f'{TMDB_BASE_URL}/person/{actor_id}/movie_credits', params={
            'api_key': API_KEY
        })
        movies = response.json()['cast']
        roles = {}
        for movie in movies:
            movie_id = movie['id']
            response = requests.get(f'{TMDB_BASE_URL}/movie/{movie_id}/credits', params={
                'api_key': API_KEY
            })
            credits = response.json()['cast']
            for credit in credits:
                if credit['name'] == actor_name:
                    role_name = credit['character']
                    if role_name not in roles:
                        roles[role_name] = []
                    roles[role_name].append(movie['title'])
        if len(roles) > 1:
            actors_roles[actor_name] = [{"movieName": movie, "characterName": role} for role, movies in roles.items() for movie in movies]
    return jsonify(actors_roles)

@app.route('/charactersWithMultipleActors', methods=['GET'])

def characters_with_multiple_actors():
    response = requests.get(f'{TMDB_BASE_URL}/movie/popular', params={
        'api_key': API_KEY
    })
    popular_movies = response.json()['results']
    characters_actors = {}
    for movie in popular_movies:
        movie_id = movie['id']
        response = requests.get(f'{TMDB_BASE_URL}/movie/{movie_id}/credits', params={
            'api_key': API_KEY
        })
        credits = response.json()['cast']
        for credit in credits:
            character_name = credit['character']
            actor_name = credit['name']
            if character_name not in characters_actors:
                characters_actors[character_name] = []
            characters_actors[character_name].append({"movieName": movie['title'], "actorName": actor_name})
    multiple_actors = {character: actors for character, actors in characters_actors.items() if len(actors) > 1}
    return jsonify(multiple_actors)

if __name__ == '__main__':
    app.run()