from django.db import models


class Category(models.Model):
    """Products will be sorted under categories
    Methods:
        get_all_categories - returns a queryset of category objects
        __str__ functions returns the name in a string format"""
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        """ Meta data instructions """
        verbose_name_plural = 'categories'  # Stops Django from adding an s after category

    def __str__(self):
        return self.name
