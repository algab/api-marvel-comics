import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.character import Character

load_dotenv()

def generate_request():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_characters(limit, offset):
    timestamp, public_key, hash = generate_request()
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
        for character in response.json()['data']['results']:
            characters.append(Character(
                id=character['id'],
                name=character['name'],
                description=character['description']
            ))
        return characters    
    else:
        return None

def search_character(id):
    timestamp, public_key, hash = generate_request()
    response = requests.get('http://gateway.marvel.com/v1/public/characters/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        character = response.json()['data']['results'][0]
        return Character(
            id=character['id'],
            name=character['name'],
            description=character['description']
        )    
    else:
        return None