from graphene import ObjectType, Schema, List, Field, ID, Int

from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.event import Event
from app.types.series import Series
from app.types.storie import Storie

import app.resolvers.character as resolve_character 
import app.resolvers.comics as resolve_comics
import app.resolvers.creator as resolve_creator
import app.resolvers.event as resolve_event
import app.resolvers.series as resolve_series
import app.resolvers.storie as resolve_storie

class Query(ObjectType):
    characters = List(Character, limit=Int(required=True), offset=Int())
    searchCharacter = Field(Character, id=ID(required=True), resolver=resolve_creator.search_creator)
    characterComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int())
    characterEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int())
    characterSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int())
    characterStories = List(Storie, id=ID(required=True), limit=Int(required=True), offset=Int())

    comics = List(Comics, limit=Int(required=True), offset=Int())
    searchComics = Field(Comics, id=ID(required=True), resolver=resolve_comics.search_comics)
    comicsCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int())
    comicsCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int())
    comicsEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int())
    comicsStories = List(Storie, id=ID(required=True), limit=Int(required=True), offset=Int())

    creators = List(Creator, limit=Int(required=True), offset=Int())
    searchCreator = Field(Creator, id=ID(required=True), resolver=resolve_creator.search_creator)
    creatorComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int())
    creatorEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int())
    creatorSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int())
    creatorStories = List(Storie, id=ID(required=True), limit=Int(required=True), offset=Int())

    events = List(Event, limit=Int(required=True), offset=Int())
    searchEvent = Field(Event, id=ID(required=True), resolver=resolve_event.search_event)
    eventCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int())
    eventComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int())
    eventCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int())
    eventSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int())
    eventStories = List(Storie, id=ID(required=True), limit=Int(required=True), offset=Int())

    series = List(Series, limit=Int(required=True), offset=Int())
    searchSerie = Field(Series, id=ID(required=True), resolver=resolve_series.search_serie)
    serieCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int())
    serieComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int())
    serieCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int())
    serieEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int())
    serieStories = List(Storie, id=ID(required=True), limit=Int(required=True), offset=Int())
    
    stories = List(Storie, limit=Int(required=True), offset=Int())
    searchStorie = Field(Storie, id=ID(required=True), resolver=resolve_storie.search_storie)
    storieCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int())
    storieComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int())
    storieCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int())
    storieEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int())
    storieSeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int())

    def resolve_characters(root, info, limit=None, offset=None):
        return resolve_character.list_characters(limit, offset)

    def resolve_characterComics(root, info, id, limit, offset=None):
        return resolve_character.find_character_comics(id, limit, offset)    

    def resolve_characterEvents(root, info, id, limit, offset=None):
        return resolve_character.find_character_events(id, limit, offset)

    def resolve_characterSeries(root, info, id, limit, offset=None):
        return resolve_character.find_character_series(id, limit, offset)

    def resolve_characterStories(root, info, id, limit, offset=None):
        return resolve_character.find_character_stories(id, limit, offset)            

    def resolve_comics(root, info, limit=None, offset=None):
        return list_comics(limit, offset)

    def resolve_comicsCharacters(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_characters(id, limit, offset)    

    def resolve_comicsCreators(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_creators(id, limit, offset)

    def resolve_comicsEvents(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_events(id, limit, offset)

    def resolve_comicsStories(root, info, id, limit, offset=None):
        return resolve_comics.find_comics_stories(id, limit, offset)

    def resolve_creators(root, info, limit=None, offset=None):
        return resolve_creator.list_creators(limit, offset)

    def resolve_creatorComics(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_comics(id, limit, offset)

    def resolve_creatorEvents(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_events(id, limit, offset)

    def resolve_creatorSeries(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_series(id, limit, offset)

    def resolve_creatorStories(root, info, id, limit, offset=None):
        return resolve_creator.find_creator_stories(id, limit, offset)

    def resolve_events(root, info, limit=None, offset=None):
        return resolve_event.list_events(limit, offset)

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

    def resolve_series(root, info, limit=None, offset=None):
        return resolve_series.list_series(limit, offset)

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

    def resolve_stories(root, info, limit=None, offset=None):
        return resolve_storie.list_stories(limit, offset)

    def resolve_storieCharacters(root, info, id, limit, offset=None):
        return resolve_storie.find_storie_characters(id, limit, offset)

    def resolve_storieComics(root, info, id, limit, offset=None):
        return resolve_storie.find_storie_comics(id, limit, offset)

    def resolve_storieCreators(root, info, id, limit, offset=None):
        return resolve_storie.find_storie_creators(id, limit, offset)

    def resolve_storieEvents(root, info, id, limit, offset=None):
        return resolve_storie.find_storie_events(id, limit, offset)

    def resolve_storieSeries(root, info, id, limit, offset=None):
        return resolve_storie.find_storie_series(id, limit, offset)    

schema = Schema(query=Query)