import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'en_US',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def get_api_key():
    api_key = input("Enter your tmdb api key:")
    return api_key


def find_movie(movie_id, api_key=''):
    api_key = api_key or get_api_key()
    movie = make_tmdb_api_request("/movie/{}".format(movie_id), api_key)
    return movie



