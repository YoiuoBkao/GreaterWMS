from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from goods.models import Goods
from supplier.models import Supplier
from .models import AsnList, AsnDetail

class AsnModelTest(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(
            supplier_name='测试供应商',
            supplier_city='上海',
            supplier_address='上海市',
            supplier_contact='张三',
            supplier_manager='李四',
            supplier_level='A',
        )
        self.asn = AsnList.objects.create(
            asn_code='ASN20240101001',
            supplier=self.supplier,
            asn_status=1,
        )

    def test_asn_creation(self):
        self.assertEqual(self.asn.asn_code, 'ASN20240101001')
        self.assertEqual(self.asn.asn_status, 1)
        self.assertEqual(str(self.asn), 'ASN20240101001')

class AsnAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.supplier = Supplier.objects.create(
            supplier_name='测试供应商',
            supplier_city='上海',
            supplier_address='上海市',
            supplier_contact='张三',
            supplier_manager='李四',
            supplier_level='A',
        )
        self.asn = AsnList.objects.create(
            asn_code='ASN20240101001',
            supplier=self.supplier,
            asn_status=1,
        )

    def test_list_asn(self):
        response = self.client.get('/api/inbound/asnlist/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_asn(self):
        data = {
            'asn_code': 'ASN20240101002',
            'supplier': self.supplier.id,
            'asn_status': 1,
            'total_weight': '0.00',
            'total_volume': '0.00',
        }
        response = self.client.post('/api/inbound/asnlist/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
