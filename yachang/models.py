# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BronzeMirror(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    desc = models.TextField()
    create_age = models.CharField(max_length=50)
    valuation = models.CharField(max_length=50)
    deal = models.CharField(max_length=100)
    auction_company = models.CharField(max_length=100)
    auction_meet = models.CharField(max_length=100)
    auction_session = models.CharField(max_length=100)
    url = models.URLField()
    file_urls = models.CharField(max_length=200)
