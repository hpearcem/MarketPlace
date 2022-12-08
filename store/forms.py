from django import forms
from store.models.category import Category
from store.models.order import Order

choices = Category.get_all_categories()


class CategoryForm(forms.Form):
    Choose_Category = forms.ModelChoiceField(
        queryset=choices,
        initial=0
        )


class QuantitySelect(forms.Form):
    quantity = forms.IntegerField(min_value=0)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_id']
