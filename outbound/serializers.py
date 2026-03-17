from rest_framework import serializers
from .models import DnList, DnDetail

class DnDetailSerializer(serializers.ModelSerializer):
    goods_code = serializers.ReadOnlyField(source='goods.goods_code')
    goods_name = serializers.ReadOnlyField(source='goods.goods_name')

    class Meta:
        model = DnDetail
        fields = '__all__'

class DnListSerializer(serializers.ModelSerializer):
    customer_name = serializers.ReadOnlyField(source='customer.customer_name')
    details = DnDetailSerializer(many=True, read_only=True, source='dndetail_set')

    class Meta:
        model = DnList
        fields = '__all__'
