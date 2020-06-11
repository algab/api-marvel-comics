import graphene

class Event(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    description = graphene.String()
    start = graphene.String()
    end = graphene.String()
    