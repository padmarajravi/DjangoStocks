# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    return render(request, 'djangostocks/templates/index.html', {})

# Create your views here.
