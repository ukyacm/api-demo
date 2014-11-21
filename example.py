from requests import get, post
import requests.auth

class BearerAuth(requests.auth.AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, response):
        response.headers['Authorization'] = 'Bearer ' + self.token
        return response

def github_user(name):
    return get("https://api.github.com/users/" + name).json()

twitter_key = 'lwYh5kfTTyI92esmWrcxwAeVC'
twitter_secret = 'y2SNNOq4UgQsnqBosfFXb9I8BuUuI1Tgs6eq7MPyBeKi5LzgWU'

def twitter_token(key, secret):
    resp = post('https://api.twitter.com/oauth2/token',
                auth=(key, secret),
                data={'grant_type': 'client_credentials'}).json()
    return resp['access_token']

def twitter_user(token, name):
    return get("https://api.twitter.com/1.1/users/show.json",
               auth=BearerAuth(token),
               params={'screen_name': name}).json()

def merge(dest, src):
    return dict(list(src.items()) + list(dest.items()))


def mashup(name):
    token = twitter_token(twitter_key, twitter_secret)
    twUser = twitter_user(token, name)
    ghUser = github_user(name)

    return merge(ghUser, twUser)
