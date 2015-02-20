# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import CategoryForm,PageForms,UserForm,UserProfileForm,DenunciaForm
from blog.models import Category,Page,UserProfile,Denuncias
from django.contrib.auth.decorators import login_required

def index(request):
	context_dict = {}	


	return render(request,"ong/index.html",{})

def add_page(request,category_name_slug):
	try:
		cat = Category.objects.get(slug=category_name_slug)
	except Category;DeosNotExist:
		cat = None

	if request.method=='POST':
		
