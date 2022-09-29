from django.contrib import admin
from .models.product import Products
from .models.category import Category


@admin.register(Products)
class ProductRegister(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("category",)
    ordering = ("name",)
    search_fields = ("name",)
    raw_id_fields = ("category",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryRegister(admin.ModelAdmin):
    pass


"""@admin.register(Order)
class OrderRegister(admin.ModelAdmin):
    date_hierarchy = "order_date"
    """

