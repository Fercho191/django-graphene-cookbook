import graphene

from ingredients.models import Category
from ingredients.nodes import CategoryNode


class CreateCategory(graphene.Mutation):
    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate(self, cls, input, context, info):
        category = Category(name=input.get('name'))
        ok = True
        return CreateCategory(category=category, ok=ok)