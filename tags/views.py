from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Tag


def tags(request):
    list = Tag.objects.all()
    return render_to_response(
        'tags/tags.html',
        locals(),
        context_instance=RequestContext(request),
    )


def tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    return render_to_response(
        'tags/tag.html',
        locals(),
        context_instance=RequestContext(request),
    )
