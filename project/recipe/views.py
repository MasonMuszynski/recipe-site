from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db import IntegrityError, transaction
from django.contrib import messages

from django.forms.formsets import formset_factory, BaseFormSet

from .models import Recipe, Step, RecipeIngredient, Ingredient
from .forms import StepForm, RecipeForm, IngredientForm


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

def add_recipe(request):
    """
    Generate a form allowing a user to add a recipe to the database
    :param request:
    :return:
    """
    user = request.user

    # Creating a formsets, allowing the form to dynamically
    # add steps and ingrediectsto the recipe
    stepFormSet = formset_factory(StepForm, formset=BaseFormSet)
    ingredientFormSet = formset_factory(IngredientForm, formset=BaseFormSet)

    if request.method == 'POST':

        # Get post information from form
        recipe_form = RecipeForm(request.POST)
        step_formset = stepFormSet(request.POST)
        ingredient_formset = ingredientFormSet(request.POST)

        if recipe_form.is_valid() and step_formset.is_valid() and ingredient_formset.is_valid():

            # getting recipe info from form and saving
            recipe = Recipe()
            recipe.name = recipe_form.cleaned_data.get('name')
            recipe.description = recipe_form.cleaned_data.get('description')
            recipe.chef = request.user
            recipe.save()

            allIngredients = []

            # iterate through each of the ingredient forms in the formset
            # and add to allIngredients array
            for ingredient_form in ingredient_formset:
                ingredientModel = ingredient_form.cleaned_data.get('model')
                quantity = ingredient_form.cleaned_data.get('quantity')
                unit = ingredient_form.cleaned_data.get('unit')
                print('ingredient iteration')

                if ingredientModel and quantity and unit:
                    allIngredients.append(RecipeIngredient(
                        ingredient=ingredientModel, recipe=recipe, quantity=quantity, unit=unit))

            try:
                with transaction.atomic():
                    RecipeIngredient.objects.bulk_create(allIngredients)

            except IntegrityError:
                messages.error(request, 'Unable to create recipe. Try again.')
                return HttpResponseRedirect('/explore/')

            allSteps = [] # array of Step model

            # iterate through each of the step forms in the formset
            # and add to allSteps array
            for step_form in step_formset:
                title = step_form.cleaned_data.get('title')
                details = step_form.cleaned_data.get('details')
                print('Step iteration')

                if title and details:
                    allSteps.append(Step(recipe=recipe, title=title, details=details))

            try:
                with transaction.atomic():
                    Step.objects.bulk_create(allSteps)

            except IntegrityError: # If transaction fails
                messages.error(request, 'Unable to create recipe. Try again.')
                return HttpResponseRedirect('/explore/')

            messages.info(request, 'Recipe create successfully.')
            return HttpResponseRedirect('/explore/')

        else:
            messages.error(request, 'Unable to create recipe. Try again.')
            return HttpResponseRedirect('/explore/')

    else:
        recipe_form = RecipeForm
        step_formset = stepFormSet
        ingredient_formset = ingredientFormSet

    context = {
        'recipe_form': recipe_form,
        'step_formset': step_formset,
        'ingredient_formset': ingredient_formset,
    }

    return render(request, 'recipe/add_recipe.html', context)

