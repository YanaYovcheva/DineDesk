from django.db import models
from django.utils.text import slugify

from menu.validators import validate_menuitem_price, validate_menuitem_title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class MenuItem(models.Model):
    title = models.CharField(max_length=100, validators=[validate_menuitem_title])
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_menuitem_price])
    image = models.ImageField(upload_to='menu', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(
                fields=["title", "category"],
                name="unique_title_category",
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
