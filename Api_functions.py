import urllib.request
import urllib.parse
import json


def load_json_data_from_url(base_url, url_params):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    response = urllib.request.urlopen(url).read().decode('utf-8')
    return json.loads(response)


def make_tmdb_api_request(method, apiKey, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'apiKey': apiKey,
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




