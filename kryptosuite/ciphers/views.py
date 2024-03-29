from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Alphabet, CipherText, Keyword
from django.urls import reverse
from .scripts import ceaser
import sys
# from django.template import loader


def clg(x):
    sys.stderr.write(x, '\n')


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


def decrypter(request):
    return render(request, 'decrypter/encode.html')


def decrypt(request):
    # clg(request.POST['ciphertext'])
    doit = ceaser.encodeCeaser
    plaintext = doit(request.POST['key'], request.POST['ciphertext'])
    context = {
        'alphabet': request.POST['alphabet'],
        'ciphertext': request.
        POST['ciphertext'],  #this only returns the first word in the string
        'key': request.POST['key'],
        'plaintext': plaintext,
    }
    # return HttpResponseRedirect("you done decrypted it:")
    return render(request, 'decrypter/answer.html', context)
    # return HttpResponse(
    #     '<p>you sent alphabet: {0}</p><p>your ciphertext was: {1} </p><p>as a key you chose: {2} </p><p>the plaintext is: {3}'
    #     .format(request.POST['alphabet'], request.POST['ciphertext'],
    #             request.POST['key'], plaintext))


# Create your views here.
