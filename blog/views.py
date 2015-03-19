# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from blog.forms import CategoryForm,PageForms,CadastroForm,DenunciaForm
from blog.models import Category,Page,Cadastro,Denuncias
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from datetime import datetime
import django.utils.encoding
import os

def index(request):
	context_dict = {}
	print "\n\n"
	print (type(request))
	print "\n\n"
	context_dict['request'] = request
	context_dict['pages'] = Page.objects.all()[:6]

	return render(request,"ong/index.html",context_dict)

#@login_required
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

#@login_required
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

		context_dict['category'] = category_slug
	except :
			print 'erro'
			context_dict['erro'] = "Erro"


	return render(request, 'ong/category.html', context_dict)

def page(request,category_slug, page_url):
	context_dict= {}

	try:
		context_dict['page']= Page.objects.filter(url=page_url)[0]
	except:
		context_dict['page']= Page.objects.filter(url=page_url)

	return render(request,'ong/artigo.html',context_dict)

def administracao(request):

	return render (request, 'ong/administracao.html',{})

def denuncie(request):
	context_dict = {}

	if request.method == 'POST':
		form = DenunciaForm (request.POST)

		if form.is_valid():
			form.save(commit=True)
			
		else:
			print form.errors
	else:
		form = DenunciaForm()

	return render(request,'ong/denuncie.html',{'formPage':form})

def contato (request):
	context_dict = {}
	return render(request,'ong/contato.html', context_dict) 