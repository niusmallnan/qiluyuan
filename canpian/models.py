# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models

# Create your models here.

class Canpian(models.Model):
    COMPLETE = 'complete'
    INCOMPLETE = 'incomplete'
    COMPLETE_CHOICES = (
	(COMPLETE, '完整'),
	(INCOMPLETE, '残缺'),
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qly_id = models.PositiveIntegerField(verbose_name='本地编号')
    name = models.CharField(max_length=60, verbose_name='名称')
    dynasty = models.ForeignKey('Dynasty', on_delete=models.CASCADE, verbose_name='年代')
    weight = models.FloatField(verbose_name='重量', help_text='单位克')
    diameter = models.FloatField(verbose_name='直径', help_text='单位厘米')
    thickness = models.FloatField(verbose_name='厚度', help_text='单位毫米')
    remark = models.TextField(verbose_name='备注')
    completeness = models.CharField(max_length=10, choices=COMPLETE_CHOICES, 
				    default=INCOMPLETE, verbose_name='是否完整')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    #deleted_at = models.DateTimeField()

    def __unicode__(self):
        return self.name

    class Meta:
	verbose_name = '铜镜残片'
        verbose_name_plural = '铜镜残片'


class Dynasty(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, verbose_name='名称')
    start_year = models.SmallIntegerField(verbose_name='开始年份')
    end_year = models.SmallIntegerField(verbose_name='终止年份')
    
    def __unicode__(self):
        return self.name

    class Meta:
	verbose_name = '年代'
        verbose_name_plural = '年代'


