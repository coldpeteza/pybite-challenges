import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_data = []
    for file in files:
        with open(file, 'r') as movie:
            movie_data.append(json.load(movie))

    return movie_data


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    comedy_movie = None
    for movie in movies:
        if 'Comedy' in movie['Genre'].split(', '):
            comedy_movie = movie['Title']
    return comedy_movie


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    nominations = dict()
    for movie in movies:
        nomination_part = movie['Awards'].split(' & ')[1]
        nomination = int(nomination_part.split(' ')[0])
        nominations[nomination] = movie['Title']
    key = max(nominations.keys())
    return f'{nominations[key]}'


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    runtimes = dict()
    for movie in movies:
        runtime = int(movie['Runtime'].split(' min')[0])
        runtimes[runtime] = movie['Title']
    key = max(runtimes.keys())
    return f'{runtimes[key]}'
