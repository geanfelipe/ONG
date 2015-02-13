# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	return HttpResponse("<br> <h1>WELCOME TO Vai Q Cola ONG </h1></br>")

