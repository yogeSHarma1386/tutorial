from django.conf.urls import include, url
from django.views import generic
from material.frontend import modules as frontend_material_urls
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)
