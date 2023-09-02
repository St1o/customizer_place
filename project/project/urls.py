from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from shoes import views
from shoes import urls as shoes_urls
from collection import urls as collection_urls
from owner import urls as owner_urls
from client import urls as client_urls
from orders import urls as orders_urls


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index),  # /store pour afficher l'index de la vue depuis views.py
                  path('shoes/', include(shoes_urls), name='shoes'),
                  path('collection/', include(collection_urls), name='collection'),
                  path('auth/', include(owner_urls), name='auth'),
                  path('client/', include(client_urls), name='client'),
                  path('orders/', include(orders_urls), name='orders'),

              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('debug/', include(debug_toolbar.urls)),
    ]
