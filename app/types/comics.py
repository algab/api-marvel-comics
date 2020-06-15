import graphene

from app.types.url import Url

class Comics(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    description = graphene.String()
    format = graphene.String()
    pageCount = graphene.Int()
    urls = graphene.List(Url)

    def resolve_urls(root, info):
        urls = []
        for data in root.urls:
            urls.append(Url(type=data['type'], url=data['url']))
        return urls
