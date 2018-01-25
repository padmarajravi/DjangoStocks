# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.contrib import admin
from djangostocks.models import Company,Stocks

admin.site.register(Company)
admin.site.register(Stocks)

# Register your models here.
