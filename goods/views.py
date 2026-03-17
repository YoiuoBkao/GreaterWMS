from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods
from .serializers import GoodsSerializer

class GoodsViewSet(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['goods_code', 'goods_class', 'goods_brand', 'is_delete']
    search_fields = ['goods_code', 'goods_name', 'goods_brand']
    ordering_fields = ['create_time', 'update_time', 'goods_code']
    ordering = ['-create_time']

    def get_queryset(self):
        return Goods.objects.filter(is_delete=False)
