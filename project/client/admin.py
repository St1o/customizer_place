from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'telephone', 'created_at', 'is_active',)
    fields = ('name', 'telephone', 'email', 'is_active')
