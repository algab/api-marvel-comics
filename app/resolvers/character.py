import requests

from app.types.character import Character

from app.utils.keys import generate_keys

def list_characters(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
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
            urls=data['urls']
        )    
    else:
        return None
