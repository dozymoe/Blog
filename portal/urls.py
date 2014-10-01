from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import index as blog_index

urlpatterns = patterns(
    '',
    url(r'^markdown/', include('django_markdown.urls')),  # noqa
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', blog_index, name='home'),
    url(r'post/', include('blog.urls', namespace='blog')),
)
