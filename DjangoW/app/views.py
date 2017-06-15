"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from Crypto.Random import random
from app.ocb import *

def home(request):
    """Renders the home page."""
    key = '000102030405060708090A0B0C0D0E0F'
    nonce = 'BBAA99887766554433221103'
    associated = ''
    #if request.GET.get('U'):
    #    message = 'You submitted: %r' % request.GET['U']
    #else:
    #    message = 'You submitted nothing'
    #UID = ''+request.GET.get('U').upper().encode()
    #TF = binascii.hexlify(request.GET.get('TF').upper())
    #TS = ''+request.GET.get('TS')
    #RLC = request.GET.get('RLC')
    PT = "%s%s%s%s" % (request.GET.get('U'),binascii.hexlify(request.GET.get('TF').upper()),request.GET.get('TS'),request.GET.get('RLC'))
    [cipher,tag] = ocb_encrypt(key,nonce,'',PT)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            #/?U=E0391122334455&TF=AA&TS=0000019B&RLC=D7B9EEA9C9FD689333AD097A9BD79C12B67A0FA6130BBC7890F12AEADF01206CB78F9DDA10A56933AE08F12588
            'namee':random.choice(['Dogs', 'Cats', 'Bears']),
            #'getu':request.GET.get('U'),
            #'gettf':binascii.hexlify(request.GET.get('TF').upper()),
            #'getts':request.GET.get('TS'),
            #'getrlc':request.GET.get('RLC'),
            'ocb': [binascii.hexlify(cipher).upper(),binascii.hexlify(tag).upper()],
            'decry': ocb_decrypt(key,nonce,associated,cipher,tag),
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
