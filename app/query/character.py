from graphene import ObjectType, List, Field, ID, Int

from app.types.character import Character
from app.types.comics import Comics
from app.types.event import Event
from app.types.series import Series
from app.types.story import Story

import app.resolvers.character as resolve_character

class QueryCharacter(ObjectType):
    characters = List(Character, limit=Int(required=True), offset=Int(), description="Fetches lists characters")
    searchCharacter = Field(Character, id=ID(required=True), description="Fetches a single character by id")
    characterComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of comics filtered by a character id")
    characterEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of events filtered by a character id")
    characterSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of series filtered by a character id")
    characterStories = List(Story, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of stories filtered by a character id")

    def resolve_characters(root, info, limit=None, offset=None):
        return resolve_character.list_characters(limit, offset)

    def resolve_searchCharacter(root, info, id):
        return resolve_character.search_character(id)

    def resolve_characterComics(root, info, id, limit, offset=None):
        return resolve_character.find_character_comics(id, limit, offset)    

    def resolve_characterEvents(root, info, id, limit, offset=None):
        return resolve_character.find_character_events(id, limit, offset)

    def resolve_characterSeries(root, info, id, limit, offset=None):
        return resolve_character.find_character_series(id, limit, offset)

    def resolve_characterStories(root, info, id, limit, offset=None):
        return resolve_character.find_character_stories(id, limit, offset)
