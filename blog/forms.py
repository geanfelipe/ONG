# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django import forms
from blog.models import Category,Page,UserProfile,Denuncias

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,help_text="Please enter the Category name")
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	slug=forms.CharField(widget=forms.HiddenInput(),required=False)

	#field slug ll be populating by the script save in models.py
	#An inline class to provide additional information on the form
	class Meta:
		#association between the model form and a model
		model = Category
		fields = ('name',)

class PageForms(forms.ModelForm):
	title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=200)
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		model = Page
		exclude = ('url',)
        #----
        #n Django 1.7+ it is now required to specify the fields that are included, via fields, or specify the fields that
        #are to be excluded, via exclude.
        #----

class UserForm(forms.ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields= ('username','email','password','email')

class UserProfileForm(forms.ModelForm)	:
	class Meta:
		model = UserProfile
		fields=('website','picture',)

class DenunciaForm(forms.ModelForm):

	class Meta:
		model = Denuncias
		fields= ('email','title','text','Category')
