# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BronzeMirror(models.Model):
    yc_id = models.CharField(max_length=50, verbose_name='雅昌编号')
    name = models.CharField(max_length=100, verbose_name='名称')
    size = models.CharField(max_length=50, verbose_name='尺寸')
    desc = models.TextField(verbose_name='信息简介')
    create_age = models.CharField(max_length=50, verbose_name='年代')
    valuation = models.CharField(max_length=50, verbose_name='估价')
    deal = models.CharField(max_length=100, verbose_name='成交价')
    auction_company = models.CharField(max_length=100, verbose_name='拍卖公司')
    auction_meet = models.CharField(max_length=100, verbose_name='拍卖会')
    auction_session = models.CharField(max_length=100, verbose_name='拍卖专场')
    auction_date = models.DateField(verbose_name='拍卖时间')
    url = models.URLField(verbose_name='雅昌网链接')
    file_urls = models.CharField(max_length=200, verbose_name='图片')

    class Meta:
        verbose_name = '铜镜拍卖'
        verbose_name_plural = '铜镜拍卖'
        ordering = ['-auction_date']

    def __unicode__(self):
        return self.name
