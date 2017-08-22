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

    # def resolve_category(self, args, context, info):
    #     id = args.get('id')
    #     name = args.get('name')
    #
    #     if id is not None:
    #         return Category.objects.get(pk=id)
    #
    #     if name is not None:
    #         return Category.objects.get(name=name)
    #
    #     return None
    #
    # def resolve_all_categories(self, args, context, info):
    #     return Category.objects.all()
    #
    # def resolve_ingredient(self, args, context, info):
    #     id = args.get('id')
    #     name = args.get('name')
    #
    #     if id is not None:
    #         return Ingredient.objects.get(pk=id)
    #
    #     if name is not None:
    #         return Ingredient.objects.get(name=name)
    #
    #     return None
    #
    # def resolve_all_ingredients(self, args, context, info):
    #     # We can easily optimize query count in the resolve method
    #     return Ingredient.objects.select_related('category').all()
