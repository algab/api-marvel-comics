import os
import requests
import hashlib
from datetime import datetime
from dotenv import load_dotenv

from app.types.creator import Creator

load_dotenv()

def generate_request():
    timestamp = str(datetime.timestamp(datetime.now()))
    public_key = os.getenv('PUBLIC_KEY')
    private_key = os.getenv('PRIVATE_KEY')
    hash = hashlib.md5('{}{}{}'.format(timestamp, private_key, public_key).encode()).hexdigest() 
    return timestamp, public_key, hash

def list_creators(limit, offset):
    timestamp, public_key, hash = generate_request()
    if limit != None and offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/creators?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(limit,offset,timestamp, public_key, hash))
    elif limit != None:
        response = requests.get('http://gateway.marvel.com/v1/public/creators?limit={}&ts={}&apikey={}&hash={}'.format(limit,timestamp, public_key, hash))
    elif offset != None:
        response = requests.get('http://gateway.marvel.com/v1/public/creators?offset={}&ts={}&apikey={}&hash={}'.format(offset,timestamp, public_key, hash))
    else:
        response = requests.get('http://gateway.marvel.com/v1/public/creators?ts={}&apikey={}&hash={}'.format(timestamp, public_key, hash))
    if response.status_code == 200:
        creators = []
        for data in response.json()['data']['results']:
            creators.append(Creator(
                id=data['id'],
                firstName=data['firstName'],
                middleName=data['middleName'],
                lastName=data['lastName'],
                suffix=data['suffix'],
                fullName=data['fullName']
            ))
        return creators    
    else:
        return None

def search_creator(id):
    timestamp, public_key, hash = generate_request()
    response = requests.get('http://gateway.marvel.com/v1/public/creators/{}?ts={}&apikey={}&hash={}'.format(id,timestamp, public_key, hash))
    if response.status_code == 200:
        creator = response.json()['data']['results'][0]
        return Creator(
            id=creator['id'],
            firstName=creator['firstName'],
            middleName=creator['middleName'],
            lastName=creator['lastName'],
            suffix=creator['suffix'],
            fullName=creator['fullName']
        )    
    else:
        return None
