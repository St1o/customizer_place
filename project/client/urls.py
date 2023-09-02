from django.urls import path

from .views import *

urlpatterns = [
    path('inscription/', inscription, name='inscription_client'),
    path('access/', access, name='access_client'),
    path('quiter/', quiter, name='logout_client'),

]