# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from blog.forms import CategoryForm,PageForms,DenunciaForm,ContatoForm
from blog.models import Category,Page,Denuncias,Contato
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from datetime import datetime
import django.utils.encoding
import os

def index(request):
	context_dict = {}
	
	if request.user.is_authenticated():
			print request.user
	else:
		print 'nao authenticated'

	context_dict['request'] = request
	context_dict['pages'] = Page.objects.all()[:6]

	return render(request,"ong/index.html",context_dict)

def index2(request):
	context_dict = {}

	return render(request,'ong/index2.html',context_dict)

def index3(request):
	context_dict = {}

	return render(request,'ong/index3.html',context_dict)


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

	return render(request,'ong/artigos/artigo.html',context_dict)

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

	context_dict['email'] = form['email']
	context_dict['title'] = form['title']
	context_dict['text'] = form['text']
	context_dict['category'] = form['Category']
	return render(request,'ong/denuncie.html',context_dict)

def contato (request):
	context_dict = {}

	if request.method =='POST':
		form = ContatoForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
		else:
			print form.errors
			context_dict['erro'] = form.errors

	else:
		form = ContatoForm()

	context_dict['nome'] = form['nome']
	context_dict['email'] = form['email']
	context_dict['mensagem'] = form['mensagem']
	return render(request,'ong/contato.html', context_dict) 


def ongs(request):
	return render(request, 'ong/ongs.html',{})

def campanhas(request):
	return render(request,'ong/campanhas.html',{})

def faca_sua_campanha(request):
	response = HttpResponse()
	response.write("<h1>OPA! ainda estamos fazendo essa <a href='/'>parte</a></h1>")
	return response
	#return render(request,'ong/facaSuaCampanha.html',{})

def lugares_verdes(request):
	return render(request,'ong/verdes.html',{})

def lugares_verdes2(request):
	return render(request,'ong/verdes2.html',{})

def eventos(request):
	return render(request,'ong/eventos.html',{})


def artigo1(request):
	return render(request,'ong/docs/artigo.html',{})

def artigo2(request):
	return render(request,'ong/docs/artigo2.html',{})
"""	
def artigo3(request):
	return render(request,'ong/artigo.html',{})
	
def artigo4(request):
	return render(request,'ong/artigo.html',{})

def artigo5(request):
	return render(request,'ong/artigo.html',{})

def artigo6(request):
	return render(request,'ong/artigo.html',{})

def artigo7(request):
	return render(request,'ong/artigo.html',{})

def artigo8(request):
	return render(request,'ong/artigo.html',{})

def artigo9(request):
	return render(request,'ong/artigo.html',{})
"""