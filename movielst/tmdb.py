import requests
import json
from urllib.parse import urlencode
from .config import *


def get_tmdb_movie(title, year):
    """ Fetch data from TMdb API. """
    OMDB_URL = 'https://api.themoviedb.org/3/search/movie?api_key=' + get_setting('API', 'TMdb_API_key') + '&'
    params = {'query': title.encode('ascii', 'ignore'),
              'language': 'en-US'}

    if year:
        params['year'] = year

    url = OMDB_URL + urlencode(params)
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"
    if r.status_code == 200:
        if "application/json" in r.headers['content-type']:
            return json.loads(r.text)
        else:
            print("Couldn't find the movie " + title)
            return None
    else:
        print("There was some error fetching info from " + url)
        return None
