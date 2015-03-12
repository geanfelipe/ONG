# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import blog.views
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples: 
    # url(r'^$', 'projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', blog.views.index, name="index"),
    url(r'^novacategoria/$', blog.views.add_category, name='nova_categoria'),
    url(r'^novapagina/$', blog.views.add_page, name='nova_pagina'),
    url(r'^Administracao/$', blog.views.administracao, name='administracao'),
    url(r'^denuncie/$', blog.views.denuncie, name='denuncie'),
    url(r'^categoria/(?P<category_slug>[\w\-]+)/$', blog.views.listarPaginas, name='listarPaginas'),
    url(r'^(?P<category_slug>[\w\-]+)/(?P<page_url>[\w\-]+)$', blog.views.page, name='pagina'),

    
    
    #url(r'^$', include(admin.blog.urls)),
)

#to upload of files Muitos sites oferecem a seus usuários com a capacidade de fazer isso - por exemplo, para fazer o upload de uma imagem de perfil
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )