import requests

from app.types.story import Story
from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.event import Event
from app.types.series import Series

from app.utils.keys import generate_keys

def list_stories(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
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

def search_storie(id):
    timestamp, public_key, hash = generate_keys()
    response = requests.get('http://gateway.marvel.com/v1/public/stories/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        story = response.json()['data']['results'][0]
        return Story(
            id=story['id'],
            title=story['title'],
            description=story['description'],
            type=story['type']
        )
    else:
        return None

def find_story_characters(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/characters?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/characters?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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

def find_story_comics(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/comics?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/comics?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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

def find_story_creators(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/creators?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/creators?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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

def find_story_events(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/events?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/events?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
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

def find_story_series(id, limit, offset):
    timestamp, public_key, hash = generate_keys()
    if offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/series?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(id, limit, offset, timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories/{}/series?limit={}&ts={}&apikey={}&hash={}'.format(id, limit, timestamp, public_key, hash))
    if response.status_code == 200:
        series = []
        for data in response.json()['data']['results']:
            series.append(Series(
                id=data['id'],
                title=data['title'],
                rating=data['rating'],
                type=data['type'],
                startYear=data['startYear'],
                endYear=data['endYear'],
                urls=data['urls']
            ))
        return series
    else:
        return None
