from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import AsnList, AsnDetail
from .serializers import AsnListSerializer, AsnDetailSerializer

class AsnListViewSet(viewsets.ModelViewSet):
    serializer_class = AsnListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['asn_status', 'supplier', 'is_delete']
    search_fields = ['asn_code', 'supplier__supplier_name']
    ordering_fields = ['create_time', 'update_time', 'asn_status']
    ordering = ['-create_time']

    def get_queryset(self):
        return AsnList.objects.filter(is_delete=False)

class AsnDetailViewSet(viewsets.ModelViewSet):
    serializer_class = AsnDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['asn', 'goods']
    search_fields = ['asn__asn_code', 'goods__goods_name', 'goods__goods_code']
    ordering_fields = ['create_time', 'update_time']
    ordering = ['-create_time']

    def get_queryset(self):
        return AsnDetail.objects.filter(asn__is_delete=False)
