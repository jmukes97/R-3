# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django import forms
from django.template import RequestContext
from django.core.urlresolvers import reverse
from .models import Post
from django.shortcuts import render
import datetime
import requests
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_edit.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def emergencey():
    url = "https://api.twilio.com/2010-04-01/Accounts/AC8e1de6b5082dd869e0a6f3399d267527/Messages.json"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"To\"\r\n\r\n13137278191\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"From\"\r\n\r\n13132511267\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Body\"\r\n\r\nI am in immediate danger. You are recieving this text because this contact has listed you as an emergency contact. If you believe this to be life threating please call the police. \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'authorization': "Basic QUM4ZTFkZTZiNTA4MmRkODY5ZTBhNmYzMzk5ZDI2NzUyNzo0NjhmZWQ1ZmFiYTNkY2I1MmI2MzcyZDUwYjQxNDA5NQ==",
    'cache-control': "no-cache",
    'postman-token': "0c4f5c00-5c43-a5fd-a7ed-cfb54690bdb5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
    #make a pop up tell the user tha the message has been sent

def confirm(request):
        if request.method == "GET":
            emergencey()
        return redirect(post_list)
