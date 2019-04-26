import requests


def get(url):
    r = requests.get(url)
    platser = r.json()
    return platser

