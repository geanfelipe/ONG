# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from blog.forms import CategoryForm,PageForms,UserForm,UserProfileForm,DenunciaForm
from blog.models import Category,Page,UserProfile,Denuncias
from django.contrib.auth.decorators import login_required

def index(request):
	context_dict = {}	


	return render(request,"ong/index.html",{})


@login_required
def add_category(self):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return TemplateResponse('ong/index.html',{})
	else:
		form = CategoryForm()

	return render(request, 'ong/newCategory.html',{})

@login_required
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

