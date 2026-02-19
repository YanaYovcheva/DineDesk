from django import forms
from menu.models import Category, MenuItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
        }


class CategoryEditForm(CategoryForm):
    ...


class CategoryCreateForm(CategoryForm):
    ...


class CategoryDeleteForm(CategoryForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        exclude = ['slug', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter menu item title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter menu item description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter menu item price'}),
            'ingredients': forms.Textarea(attrs={'placeholder': 'Enter menu item ingredients'}),
        }


class MenuItemCreateForm(MenuItemForm):
    ...

class MenuItemEditForm(MenuItemForm):
    ...

class MenuItemDeleteForm(MenuItemForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True