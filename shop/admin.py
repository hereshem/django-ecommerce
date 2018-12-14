from django.contrib import admin

# Register your models here.

from .models import Category, Product, Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
