from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['customer_city', 'customer_level', 'is_delete']
    search_fields = ['customer_name', 'customer_contact', 'customer_manager']
    ordering_fields = ['create_time', 'update_time', 'customer_name']
    ordering = ['-create_time']

    def get_queryset(self):
        return Customer.objects.filter(is_delete=False)
