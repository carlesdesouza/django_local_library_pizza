from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField(default=0)
    ingredients = models.CharField(max_length=500)
    vegetarian = models.BooleanField(default=False)
    objects = None

    # def __str__(self):
    #     return self.name, self.ingredients, self.vegetarian, self.price
