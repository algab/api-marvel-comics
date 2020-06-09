import graphene

class Creator(graphene.ObjectType):
    id = graphene.ID(required=True)
    firstName = graphene.String()
    middleName = graphene.String()
    lastName = graphene.String()
    suffix = graphene.String()
    fullName = graphene.String()
