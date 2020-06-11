import graphene

from app.types.url import Url

class Character(graphene.ObjectType):    
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    description = graphene.String()
    urls = graphene.List(Url)

    def resolve_urls(root, info):
        urls = []
        for data in root.urls:
            urls.append(Url(type=data['type'], url=data['url']))
        return urls    
