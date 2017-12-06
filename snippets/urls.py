from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import view_sets as routered_vs
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.include_format_suffixes = False

schema_view = get_schema_view(title='Pastebin API')

# Serializers
urlpatterns = [

    # Snippet Serializers
    url(r'^snippets-funxn/$', views.func_snippet_list),
    url(r'^snippets-funxn/(?P<pk>[0-9]+)$', views.func_snippet_detail),

    url(r'^snippets-class/$', views.klass_snippet_list),
    url(r'^snippets-class/(?P<pk>[0-9]+)$', views.klass_snippet_detail),

    url(r'^snippets-mixin/$', views.mixin_snippet_list),
    url(r'^snippets-mixin/(?P<pk>[0-9]+)$', views.mixin_snippet_detail),

    url(r'^snippets-generic-apiView/$', views.generic_api_view_snippet_list, name='snippet-list'),
    url(r'^snippets-generic-apiView/(?P<pk>[0-9]+)$', views.generic_api_view_snippet_detail, name='snippet-detail'),

    # User Serializers
    url(r'^users-generic-apiView/$', views.generic_api_view_user_list, name='user-list'),
    url(r'^users-generic-apiView/(?P<pk>[0-9]+)/$', views.generic_api_view_user_detail, name='user-detail'),
]

# Hyper Linked Serializers
urlpatterns += [

    url(r'^snippets-h-generic-apiView/$', views.h_generic_api_view_snippet_list, name='h-snippet-list'),
    url(r'^snippets-h-generic-apiView/(?P<pk>[0-9]+)$', views.h_generic_api_view_snippet_detail,
        name='h-snippet-detail'),

    url(r'^users-h-generic-apiView/$', views.h_generic_api_view_user_list, name='h-user-list'),
    url(r'^users-h-generic-apiView/(?P<pk>[0-9]+)/$', views.h_generic_api_view_user_detail, name='h-user-detail'),
]

# Model View Sets
urlpatterns += [

    url(r'^snippets-vs/$', views.vs_snippet_list, name='vs-snippet-list'),
    url(r'^snippets-vs/(?P<pk>[0-9]+)$', views.vs_snippet_detail, name='vs-snippet-detail'),

    url(r'^users-vs/$', views.vs_user_list, name='vs-user-list'),
    url(r'^users-vs/(?P<pk>[0-9]+)/$', views.vs_user_detail, name='vs-user-detail'),
]

# Router(ed) Model View Sets
router.register(r'r-vs-snippets', routered_vs.SnippetViewSet, base_name='r-vs-snippet')
router.register(r'r-vs-users', routered_vs.UserViewSet, base_name='r-vs-user')

urlpatterns += [
    # Include this
    url(r'^', include(router.urls))

    # OR this
    # url(r'^$', views.api_root),
]

#
urlpatterns += [
    url(r'^schema/$', schema_view),
]

# Common
urlpatterns += [

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^h-snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='h-snippet-highlight'),

    url(r'^vs-snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='vs-snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
