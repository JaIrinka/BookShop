from django.core.validators import MinValueValidator
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(to=Book, through='Catalog')


class Catalog(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    shop = models.ForeignKey(to=Shop, on_delete=models.CASCADE)
    count = models.IntegerField(validators=[MinValueValidator(0)])
