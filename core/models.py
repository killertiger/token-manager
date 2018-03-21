# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CodeGenerated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True)
    code = models.CharField(max_length=10)
    metadata = models.TextField(max_length=1000)
