from django.contrib import admin
from catalog.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = tuple('id name price category'.split())
    search_fields = ('name', 'description')
    list_filter = ('category',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = tuple('name description'.split())
