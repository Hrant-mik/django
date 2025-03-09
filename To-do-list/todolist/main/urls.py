
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,  name='index'),
    path('', views.set_cookie, name='set_cookie'),
    path('', views.get_cookie, name='get_cookie'),
]