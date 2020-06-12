from graphene import ObjectType, List, Field, ID, Int

from app.types.story import Story
from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator
from app.types.event import Event
from app.types.series import Series

import app.resolvers.story as resolve_story

class QueryStory(ObjectType):
    stories = List(Story, limit=Int(required=True), offset=Int(), description="Fetches lists of stories")
    searchStory = Field(Story, id=ID(required=True), description="Fetches a single comic story by id")
    storyCharacters = List(Character, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of characters filtered by a story id")
    storyComics = List(Comics, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of comics filtered by a story id")
    storyCreators = List(Creator, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of creators filtered by a story id")
    storyEvents = List(Event, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of events filtered by a story id")
    storySeries = List(Series, id=ID(required=True), limit=Int(required=True), offset=Int(), description="Fetches lists of series filtered by a story id")  

    def resolve_stories(root, info, limit=None, offset=None):
        return resolve_story.list_stories(limit, offset)

    def resolve_searchStory(root, info, id):
        return resolve_story.search_storie(id)    

    def resolve_storyCharacters(root, info, id, limit, offset=None):
        return resolve_story.find_story_characters(id, limit, offset)

    def resolve_storyComics(root, info, id, limit, offset=None):
        return resolve_story.find_story_comics(id, limit, offset)

    def resolve_storyCreators(root, info, id, limit, offset=None):
        return resolve_story.find_story_creators(id, limit, offset)

    def resolve_storyEvents(root, info, id, limit, offset=None):
        return resolve_story.find_story_events(id, limit, offset)

    def resolve_storySeries(root, info, id, limit, offset=None):
        return resolve_story.find_story_series(id, limit, offset)
