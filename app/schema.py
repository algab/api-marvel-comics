from graphene import ObjectType, Schema, List, Field, ID, Int

from app.types.character import Character

from app.resolvers.character import list_characters, search_character

class Query(ObjectType):
    characters = List(Character, limit=Int(), offset=Int())
    searchCharacter = Field(Character, id=ID(required=True))

    def resolve_characters(root, info, limit=None, offset=None):
        return list_characters(limit, offset)

    def resolve_searchCharacter(root, info, id):
        return search_character(id) 

schema = Schema(query=Query)