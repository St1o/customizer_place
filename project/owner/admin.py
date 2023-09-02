from django.contrib import admin

from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'address',)
    fields = ('name', 'address',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone', 'shop', 'is_superuser', 'is_owner_shop', 'created_at')
    fields = ('name', 'telephone', 'email', 'shop', 'is_owner_shop', 'is_active')
