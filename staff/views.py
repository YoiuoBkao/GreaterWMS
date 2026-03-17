from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Staff
from .serializers import StaffSerializer

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['staff_type', 'is_delete']
    search_fields = ['staff_name', 'staff_email', 'staff_phone']
    ordering_fields = ['create_time', 'update_time', 'staff_name']
    ordering = ['-create_time']

    def get_queryset(self):
        return Staff.objects.filter(is_delete=False)
