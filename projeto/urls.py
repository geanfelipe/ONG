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
    url(r'^dia-mundial-da-agua/', blog.views.artigo1, name="artigo1"),
    url(r'^dia-mundial-das-florestas/', blog.views.artigo2, name="artigo2"),
    url(r'^page2/', blog.views.index2, name="index2"),
    url(r'^page3/', blog.views.index3, name="index3"),
    url(r'^lugares-verdes/', blog.views.lugares_verdes, name="lugares_verdes"),
    url(r'^lugares-verdes2/', blog.views.lugares_verdes2, name="lugares_verdes2"),
    url(r'^eventos/', blog.views.eventos, name="eventos"),
    url(r'^campanhas/', blog.views.campanhas, name="campanhas"),
    url(r'^faca-sua-campanha/', blog.views.faca_sua_campanha, name="faca_sua_campanha"),
    url(r'^ongs/', blog.views.ongs, name='ongs'),
    url(r'^denuncie/', blog.views.denuncie, name='denuncie'),
    url(r'^contato/', blog.views.contato, name='contato'),
    url(r'^(?P<category_slug>[\w\-]+)/$', blog.views.listarPaginas, name='listarPaginas'),
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