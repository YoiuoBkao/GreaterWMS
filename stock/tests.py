from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from goods.models import Goods
from .models import Stock

class StockModelTest(TestCase):
    def setUp(self):
        self.goods = Goods.objects.create(
            goods_code='G001',
            goods_name='测试商品',
            goods_unit='个',
            goods_class='电子',
            goods_brand='品牌A',
        )
        self.stock = Stock.objects.create(
            goods=self.goods,
            warehouse_name='主仓库',
            bin_name='A-01-01',
            goods_qty=100,
            goods_unit='个',
        )

    def test_stock_creation(self):
        self.assertEqual(self.stock.goods_qty, 100)
        self.assertEqual(self.stock.warehouse_name, '主仓库')

class StockAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.goods = Goods.objects.create(
            goods_code='G001',
            goods_name='测试商品',
            goods_unit='个',
            goods_class='电子',
            goods_brand='品牌A',
        )
        self.stock = Stock.objects.create(
            goods=self.goods,
            warehouse_name='主仓库',
            bin_name='A-01-01',
            goods_qty=100,
            goods_unit='个',
        )

    def test_list_stock(self):
        response = self.client.get('/api/stock/stock/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
