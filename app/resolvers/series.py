import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.series import Series

load_dotenv()

def generate_keys():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_series(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/series?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/series?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/series?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/series?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
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

def search_serie(id):
    timestamp, public_key, hash = generate_keys()
    response = requests.get('http://gateway.marvel.com/v1/public/series/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        serie = response.json()['data']['results'][0]
        return Series(
            id=serie['id'],
            title=serie['title'],
            rating=serie['rating'],
            type=serie['type'],
            startYear=serie['startYear'],
            endYear=serie['endYear']
        )    
    else:
        return None
