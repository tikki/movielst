import requests
import json
from urllib.parse import urlencode
from .config import *


def get_omdb_movie(title, year):
    """ Fetch data from OMDB API. """
    OMDB_URL = 'http://www.omdbapi.com/?apikey=' + get_setting('API', 'OMDb_API_key') + '&'
    params = {'t': title.encode('ascii', 'ignore'),
              'plot': 'full',
              'type': 'movie',
              'tomatoes': 'true'}

    if year:
        params['y'] = year

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