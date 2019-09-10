from django.urls import path

from . import views

app_name = 'cipher'
urlpatterns = [
    path('', views.index, name='index'),
    path('alphabets', views.detail, name='Alphabet Detail'),
    path('decrypter', views.decrypter, name='workstation'),
    path('decrypt', views.decrypt, name="decrypted")
]