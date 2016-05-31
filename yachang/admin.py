# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from .apps import MIRROR_DOMAIN
from .models import BronzeMirror


class AuctionYearListFilter(admin.SimpleListFilter):
    title = '拍卖时间'
    parameter_name = 'auction_year'

    def lookups(self, request, model_admin):
        return (
            (2016, '2016年'),
            (2015, '2015年'),
            (2014, '2014年'),
            ('other', '其它'),
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return
        if self.value() == 'other':
            return queryset.filter(auction_date__year__lte=2013)

        return queryset.filter(auction_date__year=self.value())


class BronzeMirrorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'auction_company')
    fields = ('name', 'size', 'create_age', 'valuation',
              'deal', 'desc', 'yc_link', 'display_img', 'auction_company',
              'auction_meet', 'auction_session')
    readonly_fields = fields
    list_display = ('name', 'auction_date', 'create_age', 'valuation', 'deal',
                    'auction_company')
    list_filter = (AuctionYearListFilter, 'auction_company')

    def display_img(self, obj):
        full_urls = MIRROR_DOMAIN + obj.file_urls
        return mark_safe("""<a href="%s" target="_blank">
                            <img src="%s?imageView2/2/w/600" /></a>""" % (
                            full_urls, full_urls))
    display_img.short_description = '图片'

    def yc_link(self, obj):
        return mark_safe("""<a href="%s" target="_blank">%s</a>""" % (
                            obj.url, obj.url))
    yc_link.short_description = '雅昌链接'


admin.site.register(BronzeMirror, BronzeMirrorAdmin)
