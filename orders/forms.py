from django import forms
from orders.models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']
        error_messages = {
            'quantity': {
                'min_value': 'You cannot add less than one item.',
            }
        }
