from django.db import models

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200, unique=True, verbose_name='供应商名称')
    supplier_city = models.CharField(max_length=100, verbose_name='城市')
    supplier_address = models.CharField(max_length=300, verbose_name='地址')
    supplier_contact = models.CharField(max_length=100, verbose_name='联系人')
    supplier_manager = models.CharField(max_length=100, verbose_name='负责人')
    supplier_level = models.CharField(max_length=50, verbose_name='供应商等级')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'supplier'
        verbose_name = '供应商'
        verbose_name_plural = '供应商'
        ordering = ['-create_time']

    def __str__(self):
        return self.supplier_name
