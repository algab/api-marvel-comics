import graphene

class Comics(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    description = graphene.String()
    format = graphene.String()
    pageCount = graphene.Int()