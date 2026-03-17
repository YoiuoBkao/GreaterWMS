from django.db import models

class Stock(models.Model):
    goods = models.ForeignKey(
        to='goods.Goods',
        on_delete=models.CASCADE,
        verbose_name='商品'
    )
    warehouse_name = models.CharField(max_length=200, verbose_name='仓库名称')
    bin_name = models.CharField(max_length=100, verbose_name='货位名称')
    goods_qty = models.IntegerField(default=0, verbose_name='库存数量')
    goods_unit = models.CharField(max_length=50, verbose_name='商品单位')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'stock'
        verbose_name = '库存'
        verbose_name_plural = '库存'
        ordering = ['-update_time']

    def __str__(self):
        return f"{self.goods} - {self.warehouse_name} - {self.bin_name}"
