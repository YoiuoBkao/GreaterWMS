from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import DnList, DnDetail
from .serializers import DnListSerializer, DnDetailSerializer

class DnListViewSet(viewsets.ModelViewSet):
    serializer_class = DnListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['dn_status', 'customer', 'is_delete']
    search_fields = ['dn_code', 'customer__customer_name']
    ordering_fields = ['create_time', 'update_time', 'dn_status']
    ordering = ['-create_time']

    def get_queryset(self):
        return DnList.objects.filter(is_delete=False)

class DnDetailViewSet(viewsets.ModelViewSet):
    serializer_class = DnDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['dn', 'goods']
    search_fields = ['dn__dn_code', 'goods__goods_name', 'goods__goods_code']
    ordering_fields = ['create_time', 'update_time']
    ordering = ['-create_time']

    def get_queryset(self):
        return DnDetail.objects.filter(dn__is_delete=False)
