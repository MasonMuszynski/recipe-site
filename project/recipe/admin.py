from django.contrib import admin
from .models import Recipe, Step, Ingredient, RecipeIngredient

"""
Displays ingredients in the database on admin page
Displays recipes in the databse on admin page
Inlines allow RecipeIngredient and Step to be viewed and edited under Recipe
"""


class ingredientsInline(admin.StackedInline):
    model = RecipeIngredient
    verbose_name_plural = 'Ingredients'


class stepsInline(admin.StackedInline):
    model = Step
    verbose_name_plural = 'Steps'


class recipeComponents(admin.ModelAdmin):
    inlines = [
        ingredientsInline,
        stepsInline,
    ]

admin.site.register(Ingredient)
admin.site.register(Recipe, recipeComponents)