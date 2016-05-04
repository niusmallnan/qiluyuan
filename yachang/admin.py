from django.contrib import admin

from .models import BronzeMirror

class BronzeMirrorAdmin(admin.ModelAdmin):
    pass

admin.site.register(BronzeMirror, BronzeMirrorAdmin)
