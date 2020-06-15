import graphene

from app.types.url import Url

class Creator(graphene.ObjectType):
    id = graphene.ID(required=True)
    firstName = graphene.String()
    middleName = graphene.String()
    lastName = graphene.String()
    suffix = graphene.String()
    fullName = graphene.String()
    urls = graphene.List(Url)

    def resolve_urls(root, info):
        urls = []
        for data in root.urls:
            urls.append(Url(type=data['type'], url=data['url']))
        return urls
