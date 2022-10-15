from django.db import models


class Category(models.Model):
    """Products will be sorted under categories
    Methods:
        get_all_categories - returns a queryset of category objects
        __str__ functions returns the name in a string format"""
    name = models.CharField(max_length=50)

    class Meta:
        """ Meta data instructions """
        verbose_name_plural = 'categories'  # Stops Django from adding an s after category

    @staticmethod
    def get_all_categories():
        return Category.objects.all()



    @staticmethod
    def get_category_by_id(category_id):
        return Category.objects.filter(id__in=category_id)

    def __str__(self):
        return self.name
