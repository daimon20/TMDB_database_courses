import urllib.request
import urllib.parse
import json
import FilmsComparerFunctions


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, apiKey, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': apiKey,
        'language': 'en_US',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def getApiKey():
    apiKey = input("Enter your api key:")
    return apiKey


def getMovie(movieId, apiKey=''):
    apiKey = apiKey or getApiKey()
    movie = make_tmdb_api_request('/movie/%d' % movieId, apiKey)
    return movie


def getIndexOfFilmsSimmilarity(movie, chosenMovie):
    index=0
    index+=FilmsComparerFunctions.numComperor(movie["popularity"], chosenMovie["popularity"])*0.2
    index+=FilmsComparerFunctions.numComperor(movie["vote_average"], chosenMovie["vote_average"])*0.2
    movieGenres=set([s["id"] for s in movie["genres"]])
    chosenMovieGenres=set([g["id"] for g in chosenMovie["genres"]])
    index+=FilmsComparerFunctions.collectionComperor(movieGenres, chosenMovieGenres)*0.6
    return index
