from django.contrib import admin
from .models import Category, Product, Tag, Review
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Review)

