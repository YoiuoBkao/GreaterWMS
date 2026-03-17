from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Staff

class StaffModelTest(TestCase):
    def setUp(self):
        self.staff = Staff.objects.create(
            staff_name='张三',
            staff_type='仓管员',
            staff_email='zhangsan@example.com',
            staff_phone='13800138000',
        )

    def test_staff_creation(self):
        self.assertEqual(self.staff.staff_name, '张三')
        self.assertEqual(str(self.staff), '张三')
        self.assertFalse(self.staff.is_delete)

class StaffAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.staff = Staff.objects.create(
            staff_name='张三',
            staff_type='仓管员',
            staff_email='zhangsan@example.com',
            staff_phone='13800138000',
        )

    def test_list_staff(self):
        response = self.client.get('/api/staff/staff/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_staff(self):
        data = {
            'staff_name': '李四',
            'staff_type': '叉车司机',
            'staff_email': 'lisi@example.com',
            'staff_phone': '13900139000',
        }
        response = self.client.post('/api/staff/staff/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
