import graphene

from app.types.url import Url

class Event(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    description = graphene.String()
    start = graphene.String()
    end = graphene.String()
    urls = graphene.List(Url)

    def resolve_urls(root, info):
        urls = []
        for data in root.urls:
            urls.append(Url(type=data['type'], url=data['url']))
        return urls
