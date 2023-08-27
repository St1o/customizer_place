from django.urls import path

from .views import *

urlpatterns = [
    path('inscription/', inscription, name='inscription'),
    path('access/', access, name='access'),
    path('quiter/', quiter, name='logout'),
    path('owner/list', get_articles_by_owner, name='owner_list'),
    path('owner/shoes_list', get_shoes_by_owner, name='owner_shoes_list'),
    path('owner/collection_list', get_collection_by_owner, name='owner_collection_list'),
    path('owner/all_boutik', get_all_shop_articles, name='all_shop_articles'),
    path('owner/shop_name', get_all_owner, name='owner_by_shop'),

]
