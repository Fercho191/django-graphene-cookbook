import graphene
from graphene_django.debug import DjangoDebug

import ingredients.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name='__debug')
    pass

class Mutation(ingredients.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)