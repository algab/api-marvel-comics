from graphene import ObjectType, Schema, List, Field, ID, Int

from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.event import Event
from app.types.series import Series
from app.types.storie import Storie

from app.resolvers.character import list_characters, search_character
from app.resolvers.comics import list_comics, search_comics
from app.resolvers.creator import list_creators, search_creator
from app.resolvers.event import list_events, search_event
from app.resolvers.series import list_series, search_serie
from app.resolvers.storie import list_stories, search_storie

class Query(ObjectType):
    characters = List(Character, limit=Int(), offset=Int())
    searchCharacter = Field(Character, id=ID(required=True))
    comics = List(Comics, limit=Int(), offset=Int())
    searchComics = Field(Comics, id=ID(required=True))
    creators = List(Creator, limit=Int(), offset=Int())
    searchCreator = Field(Creator, id=ID())
    events = List(Event, limit=Int(), offset=Int())
    searchEvent = Field(Event, id=ID())
    series = List(Series, limit=Int(), offset=Int())
    searchSerie = Field(Series, id=ID())
    stories = List(Storie, limit=Int(), offset=Int())
    searchStorie = Field(Storie, id=ID())

    def resolve_characters(root, info, limit=None, offset=None):
        return list_characters(limit, offset)

    def resolve_searchCharacter(root, info, id):
        return search_character(id)

    def resolve_comics(root, info, limit=None, offset=None):
        return list_comics(limit, offset)

    def resolve_searchComics(root, info, id):
        return search_comics(id)

    def resolve_creators(root, info, limit=None, offset=None):
        return list_creators(limit, offset)

    def resolve_searchCreator(root, info, id):
        return search_creator(id)

    def resolve_events(root, info, limit=None, offset=None):
        return list_events(limit, offset)

    def resolve_searchEvent(root, info, id):
        return search_event(id)

    def resolve_series(root, info, limit=None, offset=None):
        return list_series(limit, offset)

    def resolve_searchSerie(root, info, id):
        return search_serie(id)

    def resolve_stories(root, info, limit=None, offset=None):
        return list_stories(limit, offset)

    def resolve_searchStorie(root, info, id):
        return search_storie(id)                     

schema = Schema(query=Query)