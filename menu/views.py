from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from menu.forms import CategoryEditForm, CategoryCreateForm, CategoryDeleteForm
from menu.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'menu/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'menu/category_add.html'
    success_url = reverse_lazy('menu:category-list')


class CategoryEditView(UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'menu/category_edit.html'
    success_url = reverse_lazy('menu:category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    form_class = CategoryDeleteForm
    template_name = 'menu/category_delete.html'

    def get_initial(self):
        return self.object.__dict__
