import graphene

class Series(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    rating = graphene.String()
    type = graphene.String()
    startYear = graphene.String()
    endYear = graphene.String()
