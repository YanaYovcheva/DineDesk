from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from menu.forms import CategoryEditForm, CategoryCreateForm, CategoryDeleteForm, MenuItemCreateForm, MenuItemEditForm, \
    MenuItemDeleteForm
from menu.models import Category, MenuItem


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


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'menu/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = self.object.menuitem_set.all()
        return context


class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemCreateForm
    template_name = 'menu/menuitem_create.html'

    def form_valid(self, form):
        category = Category.objects.get(pk=self.kwargs['pk'])
        form.instance.category = category
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'menu:category-detail',
            kwargs={'pk': self.object.category.pk},
        )


class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'menu/menuitem_detail.html'
    context_object_name = 'item'


class MenuItemEditView(UpdateView):
    model = MenuItem
    form_class = MenuItemEditForm
    template_name = 'menu/menuitem_edit.html'

    def get_success_url(self):
        return reverse("menu:menuitem-detail", kwargs={"pk": self.object.pk})


class MenuItemDeleteView(DeleteView):
    model = MenuItem
    form_class = MenuItemDeleteForm
    template_name = 'menu/menuitem_delete.html'

    def get_success_url(self):
        return reverse(
            'menu:category-detail',
            kwargs={'pk': self.object.category.pk},
        )

    def get_initial(self):
        return self.object.__dict__
