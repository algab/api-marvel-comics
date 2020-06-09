import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.comics import Comics

load_dotenv()

def generate_request():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_comics(limit, offset):
    timestamp, public_key, hash = generate_request()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/comics?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
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

def search_comics(id):
    timestamp, public_key, hash = generate_request()
    response = requests.get('http://gateway.marvel.com/v1/public/comics/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        comics = response.json()['data']['results'][0]
        return Comics(
            id=comics['id'],
            title=comics['title'],
            description=comics['description'],
            format=comics['format'],
            pageCount=comics['pageCount']
        )    
    else:
        return None
