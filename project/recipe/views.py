from django.shortcuts import render


def index(request):

    return render(request, 'recipe/view_recipe.html')
