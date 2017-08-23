import graphene

from ingredients.models import Category, Ingredient
from ingredients.nodes import CategoryNode, IngredientNode


class CreateCategory(graphene.relay.ClientIDMutation):
    '''
    mutation (category: CreateCategoryInput!){
      createCategory(input:$category){
        category{
          name
        }
    }
    Query Variables:
    {
        "category": {
            "categoryName": "Fruit",
        }
    }
    La mutacion createIngredient recibe una variable $input definida en la mutacion,
    denotada en los Query Variables
    Las variables estan en camelCase! category_id = categoryId
    '''
    class Input:
        category_name = graphene.String(required=True)

    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        category = Category(
            name=input.get('category_name')
        )
        category.save()
        return CreateCategory(category=category)

class CreateIngredient(graphene.relay.ClientIDMutation):
    '''
    mutation ($input: CreateIngredientInput!){
      createIngredient(input:$input){
        ingredient{
          name
          notes
        }
      }
    }
    Query Variables:
    {
        "input": {
            "ingredientName": "Lemon",
            "ingredientNotes": "some notes",
            "categoryId": 2
        }
    }
    La mutacion createIngredient recibe una variable $input, denotada en los Query Variables
    Las variables estan en camelCase! category_id = categoryId
    '''

    class Input:
        category_id = graphene.ID(required=True)
        ingredient_name = graphene.String(required=True)
        ingredient_notes = graphene.String()

    ingredient = graphene.Field(IngredientNode)
    category = graphene.Field(CategoryNode)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):

        ingredient = Ingredient(
            name= input.get('ingredient_name'),
            category_id= input.get('category_id'),
            notes= input.get('ingredient_notes')
        )
        category = Category.objects.get(
            id= input.get('category_id')
        )
        ingredient.save()
        return CreateIngredient(
            ingredient=ingredient,
            category=category
        )

