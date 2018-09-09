import json
import urllib
import urllib.parse
import urllib.request
import time
import psycopg2
from pprint import pprint

conn = psycopg2.connect("dbname=roadmap")
cursor = conn.cursor()
with open('cleanmovies.json') as f:
    movies = json.load(f)

results = ''

for movie in movies:
    # {
    #     "adult": false,
    #     "backdrop_path": "/rRhoMIqgdX9wEtRUOLsqXKkH9I0.jpg",
    #     "genre_ids": [
    #         878,
    #         12,
    #         9648
    #     ],
    #     "id": 70981,
    #     "original_language": "en",
    #     "original_title": "Prometheus",
    #     "overview": "A team of explorers discover a clue to the origins of mankind on Earth, leading them on a journey to the darkest corners of the universe. There, they must fight a terrifying battle to save the future of the human race.",
    #     "popularity": 20.197,
    #     "poster_path": "/ng8ALjSDhUmwLl7vtjUWIZNQSlt.jpg",
    #     "release_date": "2012-05-30",
    #     "title": "Prometheus",
    #     "video": false,
    #     "vote_average": 6.4,
    #     "vote_count": 6351
    # }
    
    id = int(movie["id"])
    title = str(movie["title"])

    print(f'title:{movie["title"]}   id: {movie["id"]}')
    results += cursor.mogrify("insert into dependency_movie (id,title, rating, description, picture, release_date) values (%(id)s, %(title)s, %(vote_average)s, %(overview)s, %(poster_path)s, %(release_date)s);", movie).decode('utf-8')
    results += '\n'

with open('newmovies.sql', 'w') as outfile:
    outfile.write(results)
