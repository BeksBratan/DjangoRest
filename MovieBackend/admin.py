from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Movie
# Register your models here.

admin.site.register(Movie)