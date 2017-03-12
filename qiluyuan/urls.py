# -*- coding: utf-8 -*-
"""qiluyuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from common.views import MetadataView

admin.site.site_header = '栖甪苑数据管理平台'
admin.site.site_title = '栖甪苑'
admin.site.index_title = '数据管理'

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    url(r'^admin/', admin.site.urls),
    url(r'^rancher-info/$', MetadataView.as_view(), name='rancher-info')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
