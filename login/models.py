# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
    username =  models.CharField(max_length=20)
    email = models.EmailField(max_length=70,blank=True)
    password = models.CharField(max_length=200)

