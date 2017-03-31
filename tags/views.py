from django.shortcuts import render, get_object_or_404

from .models import Tag


def tags(request):
    list = Tag.objects.all()
    return render(request,
                  'tags/tags.html',
                  locals())


def tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    return render(request,
                  'tags/tag.html',
                  locals())
