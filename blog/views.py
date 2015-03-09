# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from blog.forms import CategoryForm,PageForms,CadastroForm,DenunciaForm
from blog.models import Category,Page,Cadastro,Denuncias
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from datetime import datetime
import os

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
			print form.error_class
	else:
		form = CategoryForm()

	return render(request,'ong/newCategory.html',{'form':form})


def add_page(request):
	"""Modefields-->category,title,body,url,views,when"""
	"""Formfields-->category,title,body"""
	if request.method=='POST':
		formPage = PageForms(request.POST)

		if formPage.is_valid():
			formPage.save(commit=True)

		else:
			print formPage.errors
	else:
		formPage = PageForms()
	
	return render(request,'ong/newPage.html',{'form':formPage})


def listarPaginas(request, category_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_slug)
		context_dict['category_name'] = category.name

		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
	except :
			print 'Erro'


	return render(request, 'ong/category.html', context_dict)

def administracao(request):

	return render (request, 'ong/administracao.html',{})

