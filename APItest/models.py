# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db import models

# Create your models here.
class programms(models.Model):
    name = models.CharField(max_length=100);
    coast = models.IntegerField();
    description = models.CharField(max_length=10000);

