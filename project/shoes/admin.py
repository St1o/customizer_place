from django.contrib import admin

from .models import *


class ShoesInfoAdmin(admin.StackedInline):
    model = ShoesPhoto


@admin.register(ShoesInfo)
class ShoesPhotoAdmin(admin.ModelAdmin):
    inlines = [ShoesInfoAdmin]

    class Meta:
        model = ShoesInfo


@admin.register(ShoesPhoto)
class ShoesInfoAdmin(admin.ModelAdmin):
    pass

# @admin.register(Shoes)
# class ShoesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'description', 'photo_tag', 'owner')
#     readonly_fields = ['photo_tag']
#     fields = ('name', 'price', 'description', 'photo', 'owner')

# class CategoriesShoesAdmin(admin.TabularInline):
#     model = Categories.shoes_photos.through
#
#
# @admin.register(Categories)
# class CategoriesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'price', 'description', 'name', 'owner', 'get_photos')
#
#     inlines = [
#         CategoriesShoesAdmin,
#     ]
#     exclude = ('shoes',)
#
#
# @admin.register(ShoesPhoto)
# class ShoesAdmin(admin.ModelAdmin):
#     list_display = ('photo_tag',)
