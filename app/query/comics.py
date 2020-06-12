from graphene import ObjectType, List, Field, ID, Int

from app.types.comics import Comics
from app.types.character import Character
from app.types.creator import Creator
from app.types.event import Event
from app.types.story import Story

import app.resolvers.comics as resolve_comics

class QueryComics(ObjectType):
    comics = List(Comics, limit=Int(required=True), offset=Int(), description="Fetches lists of comics")
    searchComics = Field(Comics, id=ID(required=True), description="Fetches a single comic by id")
    comicsCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of characters filtered by a comic id")
    comicsCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of creators filtered by a comic id")
    comicsEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of events filtered by a comic id")
    comicsStories = List(Story, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of stories filtered by a comic id")

    def resolve_comics(root, info, limit=None, offset=None):
        return list_comics(limit, offset)

    def resolve_searchComics(root, info, id):
        return resolve_comics.search_comics(id)    

    def resolve_comicsCharacters(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_characters(id, limit, offset)    

    def resolve_comicsCreators(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_creators(id, limit, offset)

    def resolve_comicsEvents(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_events(id, limit, offset)

    def resolve_comicsStories(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_stories(id, limit, offset)
