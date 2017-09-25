# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from .forms import signUp
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from .models import user
# Create your views here.
def newUser(request):
    if request.method == "POST":
        form = signUp(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.published_date = timezone.now()
            user.save()
            return redirect('/posts', pk=post.pk)
    else:
        form = signUp(request.POST)
    return render(request, 'signIn.html', {'form': form})

