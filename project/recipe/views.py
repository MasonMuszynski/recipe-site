from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.core.exceptions import ObjectDoesNotExist

from .models import Recipe, Step


def index(request):

    return render(request, 'recipe/view_recipe.html')

def recipe_detail(request, recipe_id):
    """ View the details of a recipe

    :param request:
    :param recipe_id: the unique id of the recipe to be viewed
    :return: if the request is valid, return a page that renders the recipe.
             otherwise, return error text
    """

    # Check if the recipe exists
    try: recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")

    # Querying database to obtain ingredients and steps of the recipe
    recipeIngreds = recipe.recipeingredient_set.all()
    recipeSteps = Step.objects.filter(recipe=recipe).order_by('id')

    return render(request, 'recipe/view_recipe.html',
                  {'recipe': recipe, 'ingredients': recipeIngreds, 'steps': recipeSteps})
