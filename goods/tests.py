from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Goods

class GoodsModelTest(TestCase):
    def setUp(self):
        self.goods = Goods.objects.create(
            goods_code='G001',
            goods_name='测试商品',
            goods_unit='个',
            goods_class='电子',
            goods_brand='品牌A',
        )

    def test_goods_creation(self):
        self.assertEqual(self.goods.goods_code, 'G001')
        self.assertEqual(str(self.goods), '测试商品')
        self.assertFalse(self.goods.is_delete)

class GoodsAPITest(APITestCase):
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

    def test_list_goods(self):
        response = self.client.get('/api/goods/goods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_goods(self):
        data = {
            'goods_code': 'G002',
            'goods_name': '新商品',
            'goods_unit': '箱',
            'goods_class': '食品',
            'goods_brand': '品牌B',
        }
        response = self.client.post('/api/goods/goods/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_goods(self):
        response = self.client.get(f'/api/goods/goods/{self.goods.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_goods(self):
        data = {'goods_name': '更新商品', 'goods_code': 'G001', 'goods_unit': '个', 'goods_class': '电子', 'goods_brand': '品牌A'}
        response = self.client.put(f'/api/goods/goods/{self.goods.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_goods(self):
        response = self.client.delete(f'/api/goods/goods/{self.goods.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
