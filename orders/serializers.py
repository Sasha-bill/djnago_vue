from rest_framework.serializers import ModelSerializer

from .models import SalesOrder


class OrderSerialiser(ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = ['amount', 'description']
