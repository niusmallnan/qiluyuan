from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Canpian, Dynasty, Image
from multiupload.admin import MultiUploadAdmin


class ImageInlineAdmin(admin.TabularInline):
    model = Image


class CanpianMultiuploadMixing(object):

    def process_uploaded_file(self, uploaded, canpian, request):
        if canpian:
            image = canpian.images.create(file=uploaded)
        else:
            image = Image.objects.create(file=uploaded, canpian=None)
        return {
            'url': image.file.url,
            'thumbnail_url': image.file.url,
            'id': image.id,
            'name': image.filename
        }


class CanpianAdmin(CanpianMultiuploadMixing, MultiUploadAdmin):
    list_filter = ('dynasty__name', 'completeness')
    search_fields = ('name',)
    list_display = ('name', 'qly_id', 'dynasty', 'weight', 
                    'diameter', 'thickness', 'completeness')
    
    inlines = [ImageInlineAdmin,]
    multiupload_form = False
    multiupload_list = False

    def delete_file(self, pk, request):
        '''
        Delete an image.
        '''
        obj = get_object_or_404(Image, pk=pk)
        return obj.delete()


admin.site.register(Canpian, CanpianAdmin)


class ImageAdmin(CanpianMultiuploadMixing, MultiUploadAdmin):
    multiupload_form = False
    multiupload_list = False


admin.site.register(Image, ImageAdmin)

class DynastyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dynasty, DynastyAdmin)

