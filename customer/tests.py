from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_name='测试客户',
            customer_city='广州',
            customer_address='广州市天河区',
            customer_contact='客户联系人',
            customer_manager='客户负责人',
            customer_level='VIP',
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.customer_name, '测试客户')
        self.assertEqual(str(self.customer), '测试客户')
        self.assertFalse(self.customer.is_delete)

class CustomerAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(
            customer_name='测试客户',
            customer_city='广州',
            customer_address='广州市天河区',
            customer_contact='客户联系人',
            customer_manager='客户负责人',
            customer_level='VIP',
        )

    def test_list_customer(self):
        response = self.client.get('/api/customer/customer/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        data = {
            'customer_name': '新客户',
            'customer_city': '深圳',
            'customer_address': '深圳市南山区',
            'customer_contact': '新联系人',
            'customer_manager': '新负责人',
            'customer_level': '普通',
        }
        response = self.client.post('/api/customer/customer/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
