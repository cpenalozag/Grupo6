from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^ubicaciones/$', views.ubicacion_list),
    url(r'^ubicaciones/(?P<pk>[0-9]+)/$', views.ubicacion_detail),

    url(r'^tipos/$', views.tipo_list),
    url(r'^tipos/(?P<pk>[0-9]+)/$', views.tipo_detail),

    url(r'^micro/$', views.micro_list),
    url(r'^micro/(?P<pk>[0-9]+)/$', views.micro_detail),

    url(r'^alertas/$', views.alerta_list),
    url(r'^alertas/(?P<pk>[0-9]+)/$', views.alerta_detail),

    url(r'^mediciones/$', views.medicion_list),
    url(r'^mediciones/(?P<pk>[0-9]+)/$', views.medicion_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)
