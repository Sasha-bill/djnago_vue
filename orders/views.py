from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import SalesOrder
from orders.serializers import OrderSerialiser


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


def orders_app(request):
    return render(request, 'main_app.html')


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerialiser




