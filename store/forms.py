from django import forms
from store.models.category import Category

choices = Category.get_all_categories()


class CategoryForm(forms.Form):
    Choose_Category = forms.ModelChoiceField(
        queryset=choices,
        initial=0
        )


class QuantitySelect(forms.Form):
    quantity = forms.IntegerField(min_value=0)

