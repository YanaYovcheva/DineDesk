from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=500)
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    class CategoryChoices(models.TextChoices):
        APPETIZER = 'appetizer', 'appetizer'
        SALAD = 'salad', 'salad'
        SOUP = 'soup', 'soup'
        MAIN = 'main', 'main'
        DESSERT = 'dessert', 'dessert'
        DRINK = 'drink', 'drink'

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CategoryChoices.choices)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.title
