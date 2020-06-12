from graphene import ObjectType, List, Field, ID, Int

from app.types.event import Event
from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.series import Series
from app.types.story import Story

import app.resolvers.event as resolve_event

class QueryEvent(ObjectType):
    events = List(Event, limit=Int(required=True), offset=Int(), description="Fetches lists of events")
    searchEvent = Field(Event, id=ID(required=True), description="Fetches a single event by id")
    eventCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of characters filtered by an event id")
    eventComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of comics filtered by an event id")
    eventCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of creators filtered by an event id")
    eventSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of series filtered by an event id")
    eventStories = List(Story, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of stories filtered by an event id")

    def resolve_events(root, info, limit=None, offset=None):
        return resolve_event.list_events(limit, offset)

    def resolve_searchEvent(root, info, id):
        return resolve_event.search_event(id)    

    def resolve_eventCharacters(root, info, id, limit, offset=None):
        return resolve_event.find_event_characters(id, limit, offset)

    def resolve_eventComics(root, info, id, limit, offset=None):
        return resolve_event.find_event_comics(id, limit, offset)

    def resolve_eventCreators(root, info, id, limit, offset=None):
        return resolve_event.find_event_creators(id, limit, offset)

    def resolve_eventSeries(root, info, id, limit, offset=None):
        return resolve_event.find_event_series(id, limit, offset)

    def resolve_eventStories(root, info, id, limit, offset=None):
        return resolve_event.find_event_stories(id, limit, offset)
