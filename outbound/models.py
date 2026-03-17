from django.db import models

class DnList(models.Model):
    dn_code = models.CharField(max_length=100, unique=True, verbose_name='DN单号')
    customer = models.ForeignKey(
        to='customer.Customer',
        on_delete=models.PROTECT,
        verbose_name='客户'
    )
    total_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='总重量')
    total_volume = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='总体积')
    dn_status = models.IntegerField(default=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'dn_list'
        verbose_name = 'DN单'
        verbose_name_plural = 'DN单'
        ordering = ['-create_time']

    def __str__(self):
        return self.dn_code


class DnDetail(models.Model):
    dn = models.ForeignKey(
        to='DnList',
        on_delete=models.CASCADE,
        verbose_name='DN单'
    )
    goods = models.ForeignKey(
        to='goods.Goods',
        on_delete=models.PROTECT,
        verbose_name='商品'
    )
    plan_qty = models.PositiveIntegerField(default=0, verbose_name='计划数量')
    pick_qty = models.PositiveIntegerField(default=0, verbose_name='拣货数量')
    shipped_qty = models.PositiveIntegerField(default=0, verbose_name='发运数量')
    goods_unit = models.CharField(max_length=50, verbose_name='单位')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'dn_detail'
        verbose_name = 'DN明细'
        verbose_name_plural = 'DN明细'
        ordering = ['-create_time']

    def __str__(self):
        return f"{self.dn.dn_code} - {self.goods.goods_name}"
