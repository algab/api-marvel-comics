from graphene import ObjectType, List, Field, ID, Int

from app.types.creator import Creator
from app.types.comics import Comics
from app.types.event import Event
from app.types.series import Series
from app.types.story import Story

import app.resolvers.creator as resolve_creator

class QueryCreator(ObjectType):
    creators = List(Creator, limit=Int(required=True), offset=Int(), description="Fetches lists of creators")
    searchCreator = Field(Creator, id=ID(required=True), description="Fetches a single creator by id")
    creatorComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of comics filtered by a creator id")
    creatorEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of events filtered by a creator id")
    creatorSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of series filtered by a creator id")
    creatorStories = List(Story, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of stories filtered by a creator id")

    def resolve_creators(root, info, limit=None, offset=None):
        return resolve_creator.list_creators(limit, offset)

    def resolve_searchCreator(root, info, id):
        return resolve_creator.search_creator(id)

    def resolve_creatorEvents(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_events(id, limit, offset)

    def resolve_creatorSeries(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_series(id, limit, offset)

    def resolve_creatorStories(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_stories(id, limit, offset)
