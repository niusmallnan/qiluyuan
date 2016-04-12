from django.contrib import admin
from .models import Canpian, Dynasty


class CanpianAdmin(admin.ModelAdmin):
    list_filter = ('dynasty__name', 'completeness')
    search_fields = ('name',)
    list_display = ('name', 'qly_id', 'dynasty', 'weight', 
                    'diameter', 'thickness', 'completeness')
    

admin.site.register(Canpian, CanpianAdmin)


class DynastyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dynasty, DynastyAdmin)

