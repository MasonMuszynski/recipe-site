from django import forms
from .models import Ingredient


class StepForm(forms.Form):
    """
    Form for individual steps in a recipe
    Used in formset
    """

    title = forms.CharField(max_length=30,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Step Title',
                                'class': 'input'}), required=True)
    details = forms.CharField(max_length=800,
                              widget=forms.Textarea(attrs={
                                'placeholder': 'Step Details',
                                'class': 'textarea',
                                'rows': '2'}), required=True)


class IngredientForm(forms.Form):
    """
    Form for each individual ingredient of the recipe
    Used in formset
    """

    model = forms.ModelChoiceField(queryset=Ingredient.objects.order_by('name'))
    quantity = forms.DecimalField(max_digits=3, decimal_places=1,min_value=0, localize=False,
                                  widget=forms.NumberInput(attrs={
                                      'style': 'width: 5rem',
                                      'placeholder': 'Qty.'
                                  }))
    unit = forms.CharField(max_length=8,
                            widget=forms.TextInput(attrs={
                                'placeholder': 'Unit',
                                'class': 'input',
                            }), required=False)


class RecipeForm(forms.Form):
    """
    Form for user to input details on a new recipe
    excludes steps, which are handled by separate formset
    """

    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(attrs={
                                'placeholder': 'Recipe Name',
                                'class': 'input is-large'}), required=True)
    description = forms.CharField(max_length=400,
                           widget=forms.Textarea(attrs={
                                'placeholder': 'Description',
                                'class': 'textarea ',
                                'rows': '2'}), required=True)


