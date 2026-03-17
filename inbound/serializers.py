from rest_framework import serializers
from .models import AsnList, AsnDetail

class AsnDetailSerializer(serializers.ModelSerializer):
    goods_code = serializers.ReadOnlyField(source='goods.goods_code')
    goods_name = serializers.ReadOnlyField(source='goods.goods_name')

    class Meta:
        model = AsnDetail
        fields = '__all__'

class AsnListSerializer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source='supplier.supplier_name')
    details = AsnDetailSerializer(many=True, read_only=True, source='asndetail_set')

    class Meta:
        model = AsnList
        fields = '__all__'
