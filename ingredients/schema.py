# cookbook/ingredients/schema.py
from graphene import relay, AbstractType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)

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
