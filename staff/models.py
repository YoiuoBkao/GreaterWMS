from django.db import models

class Staff(models.Model):
    staff_name = models.CharField(max_length=100, verbose_name='员工姓名')
    staff_type = models.CharField(max_length=50, verbose_name='员工类型')
    staff_email = models.EmailField(unique=True, verbose_name='邮箱')
    staff_phone = models.CharField(max_length=20, verbose_name='电话')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'staff'
        verbose_name = '员工'
        verbose_name_plural = '员工'
        ordering = ['-create_time']

    def __str__(self):
        return self.staff_name
