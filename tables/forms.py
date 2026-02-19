from django import forms
from django.views.generic import CreateView, DeleteView

from tables.models import Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = '__all__'


class TableCreateForm(TableForm):
    ...


class TableEditForm(TableForm):
    ...


class TableDeleteForm(TableForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True

