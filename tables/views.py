from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from tables.forms import TableEditForm, TableDeleteForm
from tables.models import Table


class TableListView(ListView):
    model = Table
    template_name = 'tables/table_list.html'
    context_object_name = 'tables'


class TableDetailView(DetailView):
    model = Table
    template_name = 'tables/table_detail.html'
    context_object_name = 'table'


class TableCreateView(CreateView):
    model = Table
    form_class = TableEditForm
    template_name = 'tables/table_create.html'
    success_url = reverse_lazy('tables:list')


class TableEditView(UpdateView):
    model = Table
    form_class = TableEditForm
    template_name = 'tables/table_edit.html'
    success_url = reverse_lazy('tables:list')


class TableDeleteView(DeleteView):
    model = Table
    form_class = TableDeleteForm
    template_name = 'tables/table_delete.html'
    success_url = reverse_lazy('tables:list')

    def get_initial(self):
        return self.object.__dict__