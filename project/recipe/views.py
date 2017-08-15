from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.core.exceptions import ObjectDoesNotExist

from .models import Recipe, Step


def explore(request):
    """
    A page to browse the existing recipes.
    Sorting and searching

    :param request:
    :return:
    """

    return render(request, 'under_construction.html', {'request':request, 'page_title':'Explore'})


def recipe_detail(request, recipe_id):
    """
    View the details of a recipe

    :param request:
    :param recipe_id: the unique id of the recipe to be viewed
    :return: if the request is valid, return a page that renders the recipe.
             otherwise, return error text
    """

    # Check if the recipe exists
    try: recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist.")

    # Querying database to obtain ingredients, steps, and chef of the recipe
    recipeIngreds = recipe.recipeingredient_set.all()
    recipeSteps = Step.objects.filter(recipe=recipe).order_by('id')
    chef = recipe.chef
    recipeName = recipe.name

    return render(request, 'recipe/view_recipe.html',
                  {'request': request, 'recipe': recipe, 'ingredients': recipeIngreds, 'steps': recipeSteps,
                   'chef': chef, 'page_title':recipeName})
