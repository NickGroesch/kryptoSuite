from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alphabets', views.detail, name='Alphabet Detail')
]