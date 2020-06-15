import requests

from app.types.comics import Comics
from app.types.character import Character
from app.types.creator import Creator
from app.types.event import Event
from app.types.story import Story

from app.utils.keys import generate_keys

def list_comics(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    if response.status_code == 200:
        comics = []
        for data in response.json()['data']['results']:
            comics.append(Comics(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                format=data['format'],
                pageCount=data['pageCount'],
                urls=data['urls']
            ))
        return comics    
    else:
        return None

def search_comics(id):
    timestamp, public_key, hash = generate_keys()
    response = requests.get('http://gateway.marvel.com/v1/public/comics/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        comics = response.json()['data']['results'][0]
        return Comics(
            id=comics['id'],
            title=comics['title'],
            description=comics['description'],
            format=comics['format'],
            pageCount=comics['pageCount'],
            urls=comics['urls']
        )    
    else:
        return None

def find_comics_characters(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/characters?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/characters?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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

def find_comics_creators(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/creators?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/creators?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        creators = []
        for data in response.json()['data']['results']:
            creators.append(Creator(
                id=data['id'],
                firstName=data['firstName'],
                middleName=data['middleName'],
                lastName=data['lastName'],
                suffix=data['suffix'],
                fullName=data['fullName'],
                urls=data['urls']
            ))
        return creators    
    else:
        return None        

def find_comics_events(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/events?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/events?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        events = []
        for data in response.json()['data']['results']:
            events.append(Event(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                start=data['start'],
                end=data['end'],
                urls=data['urls']
            ))
        return events   
    else:
        return None

def find_comics_stories(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/stories?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics/{}/stories?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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
