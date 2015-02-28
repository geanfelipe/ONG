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
			#return HttpResponse(form.errors)
	else:
		form = CategoryForm()

	return render(request,'ong/newCategory.html',{'form':form})


def add_page(request):

	if request.method=='POST':
		formPage = PageForms(request.POST)

		if formPage.is_valid():
			formPage.save(commit=True)

	return render(request,'ong/newPage.html',{})

def administracao(request):



	return render (request, 'ong/administracao.html',{})