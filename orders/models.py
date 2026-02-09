from django.db import models


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'P', 'pending'
        SERVED = 'S', 'served'

    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    items = models.ManyToManyField('menu.MenuItem')
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.price for item in self.items.all())

    def __str__(self):
        return f'Table {self.table.number}: {self.status}'

