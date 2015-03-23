from django.contrib import admin
from blog.models import Category,Page,Contato,Denuncias
from blog.forms import *
from django import forms

class categoryAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug':('name',)}
	list_display = ('name',)

class pageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class DenunciasAdmin(admin.ModelAdmin):
	list_display=('email','title','text')

class contatoAdmin(admin.ModelAdmin):
	list_display=('nome','email','mensagem')

admin.site.register (Page, pageAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(Denuncias,DenunciasAdmin)
admin.site.register(Contato,contatoAdmin)