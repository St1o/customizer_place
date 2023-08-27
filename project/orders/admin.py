from django.contrib import admin

from .models import Articles, Orders, Commandes


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('shoes', 'collections',)
    fields = ('shoes', 'collections',)


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'articles_name', 'articles_price', 'articles_photo', 'name', 'created_at',)
    fields = ('name', 'articles_name', 'articles_price',)


@admin.register(Commandes)
class CommandesAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'products', 'name',)
    fields = ('total', 'products', 'name',)
