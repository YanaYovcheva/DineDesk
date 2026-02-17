from django.db import models


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'pending'
        SERVED = 'served', 'served'
        PREPARING = 'preparing', 'preparing'
        PAID = 'paid', 'paid'

    table = models.ForeignKey('tables.Table', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def total_price(self):
        return sum(item.total_price() for item in self.order_items.all())

    def __str__(self):
        return f'Table {self.table.number}: {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField(default=1)
    price_at_time = models.DecimalField(max_digits=6, decimal_places=2)

    def total_price(self):
        return self.quantity * self.price_at_time

    def __str__(self):
        return f"{self.menu_item.title} x {self.quantity}"
