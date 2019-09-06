from django.shortcuts import render
# from django.http import HttpResponse
from .models import Alphabet, CipherTexts
# from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the ciphers index.")


def detail(request):
    alphabets = Alphabet.objects.all()
    # template = loader.get_template('ciphers/index.html')
    context = {
        'alphabets': alphabets,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'ciphers/index.html', context)


# Create your views here.
