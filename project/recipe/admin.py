from django.contrib import admin
from .models import Recipe, Step, Ingredient, RecipeIngredient

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Step)