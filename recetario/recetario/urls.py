from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^recetario/', include('recetario.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:  
    # Uncomment the next line to enable the admin:
    #url(r'^$','principal.views.lista_bebidas'),
    #url(r'^$','principal.views.index'),  
    url(r'^$','principal.views.inicio'),
    url(r'^usuarios/$','principal.views.usuarios'),
    url(r'^recetas/$','principal.views.lista_recetas'),
    url(r'^receta/(?P<id_receta>\d+)$','principal.views.detalle_receta'),    
    url(r'^sobre/$','principal.views.sobre'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
)
