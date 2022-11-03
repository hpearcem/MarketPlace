from django.db import models

from .category import Category


# TODO add check to return only products that are active ?? Is this necesarry

class Products(models.Model):
    """A table for all the products to be sold
    Attributes:
        name - name of the product
        price - the price of the product given as a decimal
        category - this is a foreign key that points to the category table
        description - a field for describing the product
        image - an image of the product and a path to where the images will be stored
        supplier - foreign key pointing to the supplier table
        received_date - To keep track of when the products were received
        cost - decimal field with the cost of the product
        is_active - boolean field to show as a product for sale if true
    Imbeded class Meta:
       Stops Django from adding an s after Product 
    Methods:
        get_product_by_id - gets the product using the id field
        get_al_products - gets a queryset of all products
        get_all_products_by_category_id - does a product search using the category id
        __str__ - returns the name as a string"""
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='media/products/')
    receive_date = models.DateTimeField(auto_now_add=True)  #
    cost = models.DecimalField(max_digits=8,
                               decimal_places=2)
    is_active = models.BooleanField(default=True)

    class Meta:
        """Meta data instructions"""
        verbose_name_plural = "Products"

    @staticmethod
    def get_products_by_id(ids):
        """Returns a queryset with the product selected by ID"""
        return Products.objects.get(id__in=ids)

    @staticmethod
    def get_all_products():
        """Returns a queryset with all the products in the database"""
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        """Returns a queryset with all the products with a specified category id,
        if the category id does not exist all products are returned"""
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    def __str__(self) -> str:
        return self.name
