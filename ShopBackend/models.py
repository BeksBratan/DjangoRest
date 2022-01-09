from django.db import models
import rest_framework
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent =  models.ForeignKey('self')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    title = models.CharField(max_length=100)
    descriptor = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)