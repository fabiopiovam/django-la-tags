from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.tags, name='tags'),
    url(r'^(?P<tag_name>.*?)/$', views.tag, name='tag'),
]
