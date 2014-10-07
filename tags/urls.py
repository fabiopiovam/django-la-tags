from django.conf.urls import patterns, include, url

urlpatterns = patterns('tags.views',
    url(r'^$', 'tags', name='tags'),
    url(r'^(?P<tag_name>.*?)/$', 'tag', name='tag'),
)