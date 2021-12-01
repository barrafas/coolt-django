from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(Creator)
admin.site.register(Work)

# @admin.register(Work)
# class WorkAdmin(ImportExportModelAdmin):
#     list_display = ('name', 'type', 'publisher', 'released')
#     search_fields = ('name', 'released', 'publisher')
#     #date_hierarchy = 'compra'
#     list_filter = ('type', 'publisher')
