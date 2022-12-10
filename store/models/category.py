from django.db import models  # Import models library

"""The models will crate database tables for the application. The models have been split
but can all be in one models file. Splitting the file makes scaling up easier as the application grows"""

class Category(models.Model):
    """Products will be sorted under categories
    Column:
        name: The category name
    Class:
        Meta: Meta data instructions
    Methods:
        get_all_categories:  returns a queryset of category objects
        get_category_by_id: Returns a category when searching via the category ID(argument)
        __str__ functions:  returns the name in a string format"""
    name = models.CharField(max_length=50)  # Category name

    class Meta:
        verbose_name_plural = 'categories'  # Stops Django from adding an s after category

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        return Category.objects.filter(id__in=category_id)

    def __str__(self):
        return self.name
