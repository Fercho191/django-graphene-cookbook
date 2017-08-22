import graphene

from ingredients import schema

# You can think of this as being something like your top-level urls.py file
class Query(schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)