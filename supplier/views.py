from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Supplier
from .serializers import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['supplier_city', 'supplier_level', 'is_delete']
    search_fields = ['supplier_name', 'supplier_contact', 'supplier_manager']
    ordering_fields = ['create_time', 'update_time', 'supplier_name']
    ordering = ['-create_time']

    def get_queryset(self):
        return Supplier.objects.filter(is_delete=False)
