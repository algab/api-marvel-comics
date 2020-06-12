from graphene import ObjectType, List, Field, ID, Int

from app.types.series import Series
from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.event import Event
from app.types.story import Story

import app.resolvers.series as resolve_series

class QuerySeries(ObjectType):
    series = List(Series, limit=Int(required=True), offset=Int(), description="Fetches lists of series")
    searchSerie = Field(Series, id=ID(required=True), description="Fetches a single comic series by id")
    serieCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of characters filtered by a series id")
    serieComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of comics filtered by a series id")
    serieCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of creators filtered by a series id")
    serieEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of events filtered by a series id")
    serieStories = List(Story, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of stories filtered by a series id")

    def resolve_series(root, info, limit=None, offset=None):
        return resolve_series.list_series(limit, offset)

    def resolve_searchEvent(root, info, id):
        return resolve_series.search_serie(id)    

    def resolve_serieCharacters(root, info, id, limit, offset=None):
        return resolve_series.find_serie_characters(id, limit, offset)

    def resolve_serieComics(root, info, id, limit, offset=None):
        return resolve_series.find_serie_comics(id, limit, offset)

    def resolve_serieCreators(root, info, id, limit, offset=None):
        return resolve_series.find_serie_creators(id, limit, offset)

    def resolve_serieEvents(root, info, id, limit, offset=None):
        return resolve_series.find_serie_events(id, limit, offset)

    def resolve_serieStories(root, info, id, limit, offset=None):
        return resolve_series.find_serie_stories(id, limit, offset)
