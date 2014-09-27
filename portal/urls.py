from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^markdown/', include('django_markdown.urls')),  # noqa
    url(r'^admin/', include(admin.site.urls)),
)
