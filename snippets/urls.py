from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [

    # Snippet Serializers
    url(r'^snippets-funxn/$', views.func_snippet_list),
    url(r'^snippets-funxn/(?P<pk>[0-9]+)$', views.func_snippet_detail),

    url(r'^snippets-class/$', views.klass_snippet_list),
    url(r'^snippets-class/(?P<pk>[0-9]+)$', views.klass_snippet_detail),

    url(r'^snippets-mixin/$', views.mixin_snippet_list),
    url(r'^snippets-mixin/(?P<pk>[0-9]+)$', views.mixin_snippet_detail),

    url(r'^snippets-generic-apiView/$', views.generic_api_view_snippet_list),
    url(r'^snippets-generic-apiView/(?P<pk>[0-9]+)$', views.generic_api_view_snippet_detail),


    # User Serializers
    url(r'^users-generic-apiView/$', views.generic_api_view_user_list),
    url(r'^users-generic-apiView/(?P<pk>[0-9]+)/$', views.generic_api_view_user_detail),



    # Common
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
