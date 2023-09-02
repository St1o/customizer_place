from django.contrib import admin

from .models import *


class CollectionInfoAdmin(admin.StackedInline):
    model = CollectionPhoto


@admin.register(CollectionInfo)
class CollectionPhotoAdmin(admin.ModelAdmin):
    inlines = [CollectionInfoAdmin]

    class Meta:
        model = CollectionInfo


@admin.register(CollectionPhoto)
class CollectionInfoAdmin(admin.ModelAdmin):
    pass

