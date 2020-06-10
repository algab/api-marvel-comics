import graphene
import requests

from app.types.comics import Comics
from app.types.event import Event
from app.types.series import Series
from app.types.storie import Storie
from app.types.url import Url

from app.utils.keys import generate_keys

class Character(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    description = graphene.String()
    urls = graphene.List(Url)
    comics = graphene.List(Comics, limit=graphene.Int(required=True), offset=graphene.Int())
    events = graphene.List(Event, limit=graphene.Int(required=True), offset=graphene.Int())
    series = graphene.List(Series, limit=graphene.Int(required=True), offset=graphene.Int())
    stories = graphene.List(Storie, limit=graphene.Int(required=True), offset=graphene.Int())

    def resolve_comics(root, info, limit, offset=None):
        comics = []
        timestamp, public_key, hash = generate_keys()
        if offset != None:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/comics?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(root.id, limit, offset, timestamp, public_key, hash))
        else:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/comics?limit={}&ts={}&apikey={}&hash={}'.format(root.id, limit, timestamp, public_key, hash))
        for data in response.json()['data']['results']:
            comics.append(Comics(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                format=data['format'],
                pageCount=data['pageCount']
            ))
        return comics

    def resolve_events(root, info, limit, offset=None):
        events = []
        timestamp, public_key, hash = generate_keys()
        if offset != None:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/events?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(root.id, limit, offset, timestamp, public_key, hash))
        else:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/events?limit={}&ts={}&apikey={}&hash={}'.format(root.id, limit, timestamp, public_key, hash))
        for data in response.json()['data']['results']:
            events.append(Event(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                start=data['start'],
                end=data['end']
            ))
        return events

    def resolve_series(root, info, limit, offset=None):
        series = []
        timestamp, public_key, hash = generate_keys()
        if offset != None:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/series?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(root.id, limit, offset, timestamp, public_key, hash))
        else:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/series?limit={}&ts={}&apikey={}&hash={}'.format(root.id, limit, timestamp, public_key, hash))
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

    def resolve_stories(root, info, limit, offset=None):
        stories = []
        timestamp, public_key, hash = generate_keys()
        if offset != None:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/stories?limit={}&offset={}&ts={}&apikey={}&hash={}'.format(root.id, limit, offset, timestamp, public_key, hash))
        else:
            response = requests.get('http://gateway.marvel.com/v1/public/characters/{}/stories?limit={}&ts={}&apikey={}&hash={}'.format(root.id, limit, timestamp, public_key, hash))
        for data in response.json()['data']['results']:
            stories.append(Storie(
                id=data['id'],
                title=data['title'],
                description=data['description'],
                type=data['type']
            ))
        return stories   

    def resolve_urls(root, info):
        urls = []
        for data in root.urls:
            urls.append(Url(type=data['type'], url=data['url']))
        return urls    