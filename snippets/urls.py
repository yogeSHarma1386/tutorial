from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^snippets-funxn/$', views.func_snippet_list),
    url(r'^snippets-funxn/(?P<pk>[0-9]+)$', views.func_snippet_detail),

    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),

    url(r'^admin/', admin.site.urls)
]

urlpatterns = format_suffix_patterns(urlpatterns)
