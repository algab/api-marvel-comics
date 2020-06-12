import requests

from app.types.character import Character
from app.types.comics import Comics
from app.types.event import Event
from app.types.series import Series
from app.types.story import Story

from app.utils.keys import generate_keys

def list_characters(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    if response.status_code == 200:
        characters = []
        for data in response.json()['data']['results']:
            characters.append(Character(
                id=data['id'],
                name=data['name'],
                description=data['description'],
                urls=data['urls']
            ))
        return characters    
    else:
        return None

def search_character(id):
    timestamp, public_key, hash = generate_keys()
    response = requests.get('http://gateway.marvel.com/v1/public/characters/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        character = response.json()['data']['results'][0]
        return Character(
            id=character['id'],
            name=character['name'],
            description=character['description'],
            urls=character['urls']
        )    
    else:
        return None

def find_character_comics(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/comics?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/comics?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        comics = []
        for data in response.json()['data']['results']:
            comics.append(Comics(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                format=data['format'],
                pageCount=data['pageCount']
            ))
        return comics   
    else:
        return None

def find_character_events(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/events?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/events?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        events = []
        for data in response.json()['data']['results']:
            events.append(Event(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                start=data['start'],
                end=data['end']
            ))
        return events   
    else:
        return None

def find_character_series(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/series?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/series?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        series = []
        for data in response.json()['data']['results']:
            series.append(Series(
                id=data['id'],
                title=data['title'],
                rating=data['rating'],
                type=data['type'],
                startYear=data['startYear'],
                endYear=data['endYear']
            ))
        return series
    else:
        return None

def find_character_stories(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/stories?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/stories?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        stories = []
        for data in response.json()['data']['results']:
            stories.append(Story(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                type=data['type']
            ))
        return stories   
    else:
        return None  
