from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list/collection', views.listing, name='collection'),
    path('add', views.addCollections, name='add_collections'),
    re_path(r'^(?P<articles_id>[0-9]+)/$', views.detail, name='detail_collection'),
    re_path(r'^(?P<articles_id>[0-9]+)/delete', views.delete_by_id, name='delete_collection'),

    # path('search', views.search, name='search'),
]
