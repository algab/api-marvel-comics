from graphene import ObjectType, Schema

from app.query.character import QueryCharacter
from app.query.comics import QueryComics
from app.query.creator import QueryCreator
from app.query.event import QueryEvent
from app.query.series import QuerySeries
from app.query.story import QueryStory

class Query(QueryStory, QuerySeries, QueryEvent, QueryCreator, QueryComics, QueryCharacter, ObjectType):
    class Meta:
        description = "Query API Marvel Comics"
    pass

schema = Schema(query=Query)
