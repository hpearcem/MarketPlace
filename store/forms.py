from django import forms
from store.views import home
from store.models.category import Category

choices = Category.get_all_categories()


class CategoryForm(forms.Form):
    model_choice = forms.ModelChoiceField(
        queryset=choices,
        initial=0
        )

