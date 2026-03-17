from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from customer.models import Customer
from .models import DnList, DnDetail

class DnModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            customer_name='测试客户',
            customer_city='广州',
            customer_address='广州市',
            customer_contact='联系人',
            customer_manager='负责人',
            customer_level='VIP',
        )
        self.dn = DnList.objects.create(
            dn_code='DN20240101001',
            customer=self.customer,
            dn_status=1,
        )

    def test_dn_creation(self):
        self.assertEqual(self.dn.dn_code, 'DN20240101001')
        self.assertEqual(self.dn.dn_status, 1)
        self.assertEqual(str(self.dn), 'DN20240101001')

class DnAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(
            customer_name='测试客户',
            customer_city='广州',
            customer_address='广州市',
            customer_contact='联系人',
            customer_manager='负责人',
            customer_level='VIP',
        )
        self.dn = DnList.objects.create(
            dn_code='DN20240101001',
            customer=self.customer,
            dn_status=1,
        )

    def test_list_dn(self):
        response = self.client.get('/api/outbound/dnlist/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dn(self):
        data = {
            'dn_code': 'DN20240101002',
            'customer': self.customer.id,
            'dn_status': 1,
            'total_weight': '0.00',
            'total_volume': '0.00',
        }
        response = self.client.post('/api/outbound/dnlist/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
