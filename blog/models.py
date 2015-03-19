# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models import permalink
import datetime

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True, db_index=True)
	slug = models.SlugField(unique=True,db_index=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category,self).save(*args,**kwargs)
	
	#equals to __str__
	def __unicode__(self):
		return self.name
		#return u"%s - %d %d" %(self.name,self.views,self.likes)

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128, unique=True)
	url = models.SlugField(max_length=100 , unique=True)
	description= models.TextField(max_length=240)
	views= models.IntegerField(default=0)
	when = models.DateTimeField('data de criação', auto_now_add=True, db_index=True)
	slugCategory = models.SlugField(unique=True,db_index=True)
	body = models.TextField()

	def save(self, *args, **kwargs):
		self.url = slugify(self.title)
		self.slugCategory = slugify(self.category)
		super(Page,self).save(*args,**kwargs)

	#equals to __str__
	def __unicode__(self):
		return self.title

class Cadastro(models.Model):
	"""
	--> dedicated to ONG
	"""

	name = models.CharField(max_length=128, unique=True)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images/%Y/%m/%d',blank=True)
	email = models.EmailField(unique=True)


	def __unicode__(self):
		return self.name

class Denuncias(models.Model):
	email = models.EmailField()
	title = models.CharField(max_length=128)
	text = models.TextField()
	Category = models.CharField(max_length=128)

	def __unicode__(self):
		return self.title

class Contato(models.Model):
	nome = models.CharField(max_length=128)
	email = models.EmailField()
	mensagem = models.TextField()

 	def __unicode__(self):
 		return 'denuncia de '+self.nome