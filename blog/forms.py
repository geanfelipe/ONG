# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms
from blog.models import Category,Page,Denuncias, Contato

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,help_text="Nome da Categoria")
	#slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	class Meta:
		model = Category
		fields = ('name',)

class PageForms(forms.ModelForm):
	"""fields-->category,title,body,url,views,when"""
	title = forms.CharField(max_length=128, help_text="Título da Página")
	description = forms.CharField(widget = forms.Textarea() , help_text="Breve descrição sobre o assunto")
	body = forms.CharField(widget = forms.Textarea(), help_text= "Coluna da Página")

	class Meta:
		model = Page
		fields = ('category','title','description','body')
       

class DenunciaForm(forms.ModelForm):
	email = forms.EmailField(label="Email")
	title = forms.CharField(max_length = 100, label= "Título")
	text= forms.CharField(widget=forms.Textarea(),label = "Denúncia")
	Category = forms.CharField(max_length = 100, label  = "Tipo de sua Denúncia")
	class Meta:
		model = Denuncias
		fields= ('email','title','text','Category')

class ContatoForm(forms.ModelForm):
	nome = forms.CharField(required=True, max_length=128, label="Nome")
	email = forms.EmailField(required=True,label="E-mail")
	mensagem = forms.CharField(required=True, widget=forms.Textarea(), label="Mensagem")
	
	class Meta:
		model = Contato
		fields = ('nome','email','mensagem')