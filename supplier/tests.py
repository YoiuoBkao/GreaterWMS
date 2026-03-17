from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Supplier

class SupplierModelTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            supplier_name='测试供应商',
            supplier_city='上海',
            supplier_address='上海市浦东新区',
            supplier_contact='张三',
            supplier_manager='李四',
            supplier_level='A',
        )

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.supplier_name, '测试供应商')
        self.assertEqual(str(self.supplier), '测试供应商')
        self.assertFalse(self.supplier.is_delete)

class SupplierAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(
            supplier_name='测试供应商',
            supplier_city='上海',
            supplier_address='上海市浦东新区',
            supplier_contact='张三',
            supplier_manager='李四',
            supplier_level='A',
        )

    def test_list_supplier(self):
        response = self.client.get('/api/supplier/supplier/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_supplier(self):
        data = {
            'supplier_name': '新供应商',
            'supplier_city': '北京',
            'supplier_address': '北京市朝阳区',
            'supplier_contact': '王五',
            'supplier_manager': '赵六',
            'supplier_level': 'B',
        }
        response = self.client.post('/api/supplier/supplier/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
