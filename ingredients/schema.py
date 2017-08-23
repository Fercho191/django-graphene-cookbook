# cookbook/ingredients/schema.py
from graphene import relay, AbstractType
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.models import Ingredient
from ingredients.nodes import CategoryNode, IngredientNode


class Query(AbstractType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

    def resolve_all_ingredients(self, args, context, info):
        # If you are using GraphQLView you can access Django request with the context argument.
        # context will reference to the Django request
        if not context.user.is_authenticated():
            return Ingredient.objects.none()
        else:
            return Ingredient.objects.filter(available=True)
        # return Ingredient.objects.filter(available=True)
