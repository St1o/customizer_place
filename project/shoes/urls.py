from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/shoes', views.listing, name='shoes'),
    path('contact', views.contact, name='contact'),
    re_path(r'^(?P<articles_id>[0-9]+)/$', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path('add', views.addShoes, name='add_shoes'),
    re_path(r'^(?P<articles_id>[0-9]+)/delete', views.delete_by_id, name='delete_shoes'),
    path('update_shoes/<pk>', views.update_shoes, name='update_shoes'),

]
