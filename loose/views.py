# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def donate(request):
    return render(request, 'donate-money.html')

def donateNM(request):
    return render(request, 'donate.html')

def request(request):
    return render(request, 'request.html')
