from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, CreateView
from orders.forms import OrderItemForm
from orders.models import Order, OrderItem
from tables.models import Table


class OrderCreateView(View):
    def post(self, request, table_pk):
        table = get_object_or_404(Table, pk=table_pk)

        order = Order.objects.create(
            table=table,
            status='pending'
        )

        return redirect('orders:detail', pk=order.pk)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderItemForm()
        return context


class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm

    def form_valid(self, form):
        order = get_object_or_404(Order, pk=self.kwargs['order_pk'])
        form.instance.order = order
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('orders:detail', kwargs={'pk': self.object.order.pk})


class OrderItemDeleteView(View):
    def post(self, request, pk):
        item = get_object_or_404(OrderItem, pk=pk)
        order_pk = item.order.pk
        item.delete()

        return redirect('orders:detail', pk=order_pk)


class OrderStatusEditView(View):
    def post(self, request, pk, status):
        order = get_object_or_404(Order, pk=pk)

        valid_statuses = [choice[0] for choice in Order.StatusChoices.choices]

        if status in valid_statuses:
            order.status = status
            order.save()

        return redirect('orders:detail', pk=pk)
