import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.event import Event

load_dotenv()

def generate_keys():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_events(limit, offset):
    timestamp, public_key, hash = generate_keys()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/events?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/events?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/events?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/events?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
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

def search_event(id):
    timestamp, public_key, hash = generate_keys()
    response = requests.get('http://gateway.marvel.com/v1/public/events/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        event = response.json()['data']['results'][0]
        return Event(
            id=event['id'],
            title=event['title'],
            description=event['description'],
            start=event['start'],
            end=event['end']
        )    
    else:
        return None
