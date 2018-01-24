from django.conf.urls import url
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import view_sets as routered_vs

router = DefaultRouter()
router.include_format_suffixes = False

schema_view = get_schema_view(title='Pastebin API')

# Serializers
urlpatterns = [

    # Snippet Serializers
    url(r'^list-using-funxn/$', views.func_snippet_list),
    url(r'^detailing-using-funxn/(?P<pk>[0-9]+)$', views.func_snippet_detail),

    url(r'^list-using-class/$', views.klass_snippet_list),
    url(r'^detailing-using-class/(?P<pk>[0-9]+)$', views.klass_snippet_detail),

    url(r'^list-using-mixin/$', views.mixin_snippet_list),
    url(r'^detailing-using-mixin/(?P<pk>[0-9]+)$', views.mixin_snippet_detail),

    url(r'^list-using-generic-apiView/$',
        view=views.generic_api_view_snippet_list,
        name='snippet-list'),

    url(r'^detailing-using-generic-apiView/(?P<pk>[0-9]+)$',
        view=views.generic_api_view_snippet_detail,
        name='snippet-detail'),

    # User Serializers
    url(r'^user-list-using-apiView/$',
        view=views.generic_api_view_user_list,
        name='user-list'),

    url(r'^user-detailing-using-generic-apiView/(?P<pk>[0-9]+)/$',
        view=views.generic_api_view_user_detail,
        name='user-detail'),
]

# Hyper Linked Serializers
urlpatterns += [

    url(r'^list-using-h-generic-apiView/$',
        view=views.h_generic_api_view_snippet_list,
        name='h-snippet-list'),

    url(r'^detailing-using-h-generic-apiView/(?P<pk>[0-9]+)$',
        view=views.h_generic_api_view_snippet_detail,
        name='h-snippet-detail'),

    url(r'^user-list-using-h-generic-apiView/$',
        view=views.h_generic_api_view_user_list,
        name='h-user-list'),

    url(r'^user-detailing-using-h-generic-apiView/(?P<pk>[0-9]+)/$',
        view=views.h_generic_api_view_user_detail,
        name='h-user-detail'),
]

# Model View Sets
urlpatterns += [

    url(r'^list-using-vs/$', views.vs_snippet_list, name='vs-snippet-list'),
    url(r'^detailing-using-vs/(?P<pk>[0-9]+)$', views.vs_snippet_detail, name='vs-snippet-detail'),

    url(r'^user-list-using-vs/$', views.vs_user_list, name='vs-user-list'),
    url(r'^user-detailing-using-vs/(?P<pk>[0-9]+)/$', views.vs_user_detail, name='vs-user-detail'),
]

# Router(ed) Model View Sets
router.register(r'list-using-vs', routered_vs.SnippetViewSet, base_name='r-vs-snippet')
router.register(r'user-list-using-vs', routered_vs.UserViewSet, base_name='r-vs-user')

# Common
urlpatterns += [

    url(r'^routed/', include(router.urls), name='routed-urls'),
    url(r'^non-routed/', views.api_root, name='non-routed-urls'),

    path(r'^url-schema/$', schema_view),

    url(r'^using-generic-apiView/(?P<pk>[0-9]+)/highlight/$',
        view=views.SnippetHighlightedView.as_view(),
        name='vs-snippet-highlight'),

    # url(r'^', RedirectView.as_view(url='routed/')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
