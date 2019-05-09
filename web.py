import requests


def get(url): #gör om en url till json
    r = requests.get(url)
    platser = r.json()
    return platser

