from .config import *
from .API_util import make_request


def get_omdb_movie(title, year):
    """ Fetch data from OMDB API. """
    OMDB_URL = 'http://www.omdbapi.com/?apikey=' + get_setting('API', 'OMDb_API_key') + '&'
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

    return make_request(OMDB_URL, params, title)