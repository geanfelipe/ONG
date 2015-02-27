# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from blog.forms import CategoryForm,PageForms,CadastroForm,DenunciaForm
from blog.models import Category,Page,Cadastro,Denuncias
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from datetime import datetime

def index(request):
	context_dict = {}	


	return render(request,"ong/index.html",{})



def add_category(request):
	
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)

			return HttpResponse("<h1>Ok</h1>")
		else:
			print form.errors
			return HttpResponse("erro")
	else:
		form = CategoryForm()

	return render(request,'ong/newCategory.html',{'form':form})


def add_page(request,category_name_slug):
	try:
		cat = Category.objects.get(slug=category_name_slug)
	except Category.DeosNotExist:
		cat = None

	if request.method=='POST':
		form = PageForms(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit=False)
				page.category= cat
				page.views = 0
				page.save()
				return category(request,category_name_slug)
		else:
			print form.errors
	else:
		form = PageForms()

	context_dict = {'form':form, 'category':cat, 'link':cat.slug}

	return render(request,'ong/newPage.html',context_dict)

