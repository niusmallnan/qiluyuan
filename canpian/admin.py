from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Canpian, Dynasty, Image


class ImageInlineAdmin(admin.TabularInline):
    model = Image
    readonly_fields = ('render_image',)

    def render_image(self, obj):
        return mark_safe("""<img src="%s?imageView2/2/w/600" />""" % obj.file.url)


class CanpianAdmin(admin.ModelAdmin):
    list_filter = ('dynasty__name', 'completeness')
    search_fields = ('name',)
    list_display = ('name', 'qly_id', 'dynasty', 'weight',
                    'diameter', 'thickness', 'completeness')

    inlines = [ImageInlineAdmin,]


admin.site.register(Canpian, CanpianAdmin)


class DynastyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dynasty, DynastyAdmin)

