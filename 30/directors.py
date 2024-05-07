import csv
from collections import defaultdict, namedtuple, Counter
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = os.getenv("TMP", "/tmp")

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = defaultdict(list)
    with open(MOVIE_DATA, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            director_name = item['director_name'] if 'director_name' in item.keys() else None
            movie_title = item['movie_title'] if 'movie_title' in item.keys() else None
            movie_year = item['title_year'] if 'title_year' in item.keys() else None
            movie_score = item['imdb_score'] if 'imdb_score' in item.keys() else None

            if director_name and movie_title and movie_year and movie_score:
                if int(movie_year) > MIN_YEAR:
                    movies[director_name].append(Movie(title=movie_title, year=int(movie_year), score=float(movie_score)))

    return movies


def calc_mean_score(movies: list[Movie]):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total = 0
    for movie in movies:
        total += movie.score

    result = total / len(movies)
    return round(result, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    results = []
    for director_name, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            results.append((director_name, calc_mean_score(movies)))

    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    return sorted_results
