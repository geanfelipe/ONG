from django.contrib import admin
from blog.models import Category,Page,UserProfile,Denuncias

class categoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class pageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

class UserProfileAdmin(admin.ModelAdmin):
	list_display=('website','')

class DenunciasAdmin(admin.ModelAdmin):
	list_display=('email','title','Category')

admin.site.register (Page, pageAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(UserProfile)
admin.site.register(Denuncias,DenunciasAdmin)
