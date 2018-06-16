from django.db import models


class BuyItem(models.Model):
    ''' 買うもの '''

    name = models.CharField(max_length=255, verbose_name='商品名')
    need_count = models.IntegerField(verbose_name='必要な数')
    comment = models.TextField(
        max_length=1000, blank=True, verbose_name='コメント')
    is_purchased = models.BooleanField(default=False, verbose_name='購入済み')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新日')

    def __str__(self):
        return self.name
