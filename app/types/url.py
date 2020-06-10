import graphene

class Url(graphene.ObjectType):
    type = graphene.String(required=True)
    url = graphene.String(required=True)