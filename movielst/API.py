from .omdb import get_omdb_movie
from .tmdb import get_tmdb_movie


def get_api(title, year, external_api="omdb"):
    item = {
        "title": None,
        "genre": None,
        "imdb": None,
        "runtime": None,
        "tomato": None,
        "year": None,
        "awards": None,
        "cast": None,
        "director": None,
        "poster": None,
        "response": False
    }
    if external_api == "omdb":
        omdb = get_omdb_movie(title, year)
        if omdb['Response'] == 'True':
            item["title"] = omdb["Title"]
            item["genre"] = omdb["Genre"]
            item["imdb"] = omdb["imdbRating"]
            item["runtime"] = omdb["Runtime"]
            item["tomato"] = get_rotten_score(omdb)
            item["year"] = omdb["Year"]
            item["awards"] = omdb["Awards"]
            item["cast"] = omdb["Actors"]
            item["director"] = omdb["Director"]
            item["poster"] = omdb["Poster"]
            item['response'] = omdb["Response"]
        else:
            item['response'] = omdb["Response"]

    elif external_api == "tmdb":
        tmdb = get_tmdb_movie(title, year)
        item["title"] = tmdb["results"][0]['title']
        item["year"] = tmdb["results"][0]['release_date'].split('-', 1)[0]

        item["genre"] = "unsupported"
        item["imdb"] = "unsupported"
        item["runtime"] = "unsupported"
        item["tomato"] = "unsupported"
        item["awards"] = "unsupported"
        item["cast"] = "unsupported"
        item["director"] = "unsupported"

        genre_ids = tmdb["results"][0]['genre_ids']

    return item


def get_rotten_score(item):
    try:
        if item['Ratings'][1]['Source'] == "Rotten Tomatoes":
            return item['Ratings'][1]['Value']
        else:
            return "N/A"
    except IndexError:
        return "N/A"
