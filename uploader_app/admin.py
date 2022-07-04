from django.contrib import admin
from uploader_app.models import UploadedFile


class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'file_size', 'file_type', 'file')


admin.site.register(UploadedFile, UploadedFileAdmin)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
