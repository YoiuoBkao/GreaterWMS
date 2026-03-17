from django.db import models

class Goods(models.Model):
    goods_code = models.CharField(max_length=100, unique=True, verbose_name='商品编码')
    goods_name = models.CharField(max_length=200, verbose_name='商品名称')
    goods_unit = models.CharField(max_length=50, verbose_name='商品单位')
    goods_class = models.CharField(max_length=100, verbose_name='商品分类')
    goods_brand = models.CharField(max_length=100, verbose_name='商品品牌')
    goods_origin = models.CharField(max_length=100, blank=True, verbose_name='原产地')
    safety_stock = models.IntegerField(default=0, verbose_name='安全库存')
    goods_desc = models.TextField(blank=True, verbose_name='商品描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = '商品'
        ordering = ['-create_time']

    def __str__(self):
        return self.goods_name
