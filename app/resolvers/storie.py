import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.storie import Storie

load_dotenv()

def generate_keys():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_stories(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/stories?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
    if response.status_code == 200:
        stories = []
        for data in response.json()['data']['results']:
            stories.append(Storie(
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
        storie = response.json()['data']['results'][0]
        return Storie(
            id=storie['id'],
            title=storie['title'],
            description=storie['description'],
            type=storie['type']
        )
    else:
        return None
