from .config import *
from .API_util import make_request


def get_tmdb_movie(title, year):
    """ Fetch data from TMdb API. """
    tmdb_url = 'https://api.themoviedb.org/3/search/movie?api_key=' + get_setting('API', 'TMdb_API_key') + '&'
    params = {'query': title.encode('ascii', 'ignore'),
              'language': 'en-US'}

    if year:
        params['year'] = year
    return make_request(tmdb_url, params, title)


def get_genre(ids):
    pass
