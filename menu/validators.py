from django.core.exceptions import ValidationError


def validate_menuitem_price(value):
    if value <= 0:
        raise ValidationError('Price must be greater than 0')


def validate_menuitem_title(value):
    if len(value) < 3:
        raise ValidationError("Title must be at least 3 characters long.")

    if value.isdigit():
        raise ValidationError("Title cannot contain only numbers.")
