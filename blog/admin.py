from django.contrib import admin
from blog.models import Category,Page,Cadastro,Denuncias

class categoryAdmin(admin.ModelAdmin):
	#prepopulated_fields = {'slug':('name',)}
	list_display = ('name',)
class pageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class UserProfileAdmin(admin.ModelAdmin):
	list_display=('website','name','email')


class DenunciasAdmin(admin.ModelAdmin):
	list_display=('email','title')

admin.site.register (Page, pageAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(Cadastro)
admin.site.register(Denuncias,DenunciasAdmin)
