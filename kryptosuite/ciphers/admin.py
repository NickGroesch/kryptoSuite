from django.contrib import admin

from .models import Alphabet, CipherText, Keyword

admin.site.register(Alphabet)
admin.site.register(CipherText)
admin.site.register(Keyword)
# Register your models here.
