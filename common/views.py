from django.views.generic import TemplateView

from menu.models import MenuItem
from orders.models import Order
from tables.models import Table


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["menu_items_count"] = MenuItem.objects.count()
        context["active_orders"] = Order.objects.filter(status="pending").count()
        context["tables_count"] = Table.objects.count()

        return context