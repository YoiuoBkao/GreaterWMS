from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Stock
from .serializers import StockSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['warehouse_name', 'bin_name', 'goods']
    search_fields = ['warehouse_name', 'bin_name', 'goods__goods_name', 'goods__goods_code']
    ordering_fields = ['update_time', 'goods_qty']
    ordering = ['-update_time']
