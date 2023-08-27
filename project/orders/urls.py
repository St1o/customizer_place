from django.urls import path, re_path

from .views import *

urlpatterns = [
    re_path(r'^(?P<articles_id>[0-9]+)/$', backet, name='backet'),
    path('achat', achat, name='achat'),
    path('delete/<uuid:pk>', delete_by_uid, name='del'),
    path('paiement', paiement, name='paiement'),
    path('buy', after_paiement, name='buy'),
    path('all_commandes', allCommades, name='allcmd'),
    path('delete_cmd/<uuid:pk>', delete_by_uid_commandes, name='delcmd'),

]
