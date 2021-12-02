from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Creator)
class CreatorAdmin(ImportExportModelAdmin):
    list_display = ('creator',)
    search_fields = ('creator',)


@admin.register(Work)
class WorkAdmin(ImportExportModelAdmin):
    list_display = ('name', 'type', 'publisher', 'released')
    search_fields = ('name', 'released', 'publisher')
    #date_hierarchy = 'compra'
    list_filter = ('type', 'publisher')


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ('genre',)
    search_fields = ('genre',)


@admin.register(Work_Creator)
class Work_CreatorAdmin(ImportExportModelAdmin):
    list_display = ('work_id', 'creator_id')
    search_fields = ('work_id', 'creator_id')


@admin.register(Work_Genre)
class Work_GenreAdmin(ImportExportModelAdmin):
    list_display = ('work_id', 'genre_id')
    search_fields = ('work_id', 'genre_id')
