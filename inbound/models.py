from django.db import models

class AsnList(models.Model):
    asn_code = models.CharField(max_length=100, unique=True, verbose_name='ASN单号')
    supplier = models.ForeignKey(
        to='supplier.Supplier',
        on_delete=models.PROTECT,
        verbose_name='供应商'
    )
    total_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='总重量')
    total_volume = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='总体积')
    asn_status = models.IntegerField(default=1, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'asn_list'
        verbose_name = 'ASN单'
        verbose_name_plural = 'ASN单'
        ordering = ['-create_time']

    def __str__(self):
        return self.asn_code


class AsnDetail(models.Model):
    asn = models.ForeignKey(
        to='AsnList',
        on_delete=models.CASCADE,
        verbose_name='ASN单'
    )
    goods = models.ForeignKey(
        to='goods.Goods',
        on_delete=models.PROTECT,
        verbose_name='商品'
    )
    expected_qty = models.IntegerField(default=0, verbose_name='预计数量')
    actual_qty = models.IntegerField(default=0, verbose_name='实际数量')
    sorted_qty = models.IntegerField(default=0, verbose_name='分拣数量')
    goods_unit = models.CharField(max_length=50, verbose_name='单位')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'asn_detail'
        verbose_name = 'ASN明细'
        verbose_name_plural = 'ASN明细'
        ordering = ['-create_time']

    def __str__(self):
        return f"{self.asn.asn_code} - {self.goods.goods_name}"
