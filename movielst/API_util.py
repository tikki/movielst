import requests
from urllib.parse import urlencode
import json


def make_request(url, params, title):
    url = url + urlencode(params)
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