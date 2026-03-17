from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):
    goods_code = serializers.ReadOnlyField(source='goods.goods_code')
    goods_name = serializers.ReadOnlyField(source='goods.goods_name')

    class Meta:
        model = Stock
        fields = '__all__'
