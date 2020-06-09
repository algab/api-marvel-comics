import graphene

class Character(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    description = graphene.String()