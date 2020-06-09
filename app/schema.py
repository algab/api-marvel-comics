from graphene import ObjectType, Schema, List, Field, ID, Int

from app.types.character import Character
from app.types.comics import Comics
from app.types.creator import Creator

from app.resolvers.character import list_characters, search_character
from app.resolvers.comics import list_comics, search_comics
from app.resolvers.creator import list_creators, search_creator

class Query(ObjectType):
    characters = List(Character, limit=Int(), offset=Int())
    searchCharacter = Field(Character, id=ID(required=True))
    comics = List(Comics, limit=Int(), offset=Int())
    searchComics = Field(Comics, id=ID(required=True))
    creators = List(Creator, limit=Int(), offset=Int())
    searchCreator = Field(Creator, id=ID())

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

schema = Schema(query=Query)