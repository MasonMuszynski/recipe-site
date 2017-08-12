from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=400, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    chef = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """
    Many to Many relationship to collect more information on ingredients
    """
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3,decimal_places=1)
    unit = models.CharField(max_length=8, null=True)



class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=800)

    def __str__(self):
        return self.title
