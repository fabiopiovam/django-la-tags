from django.template import Library
from django.contrib.contenttypes.models import ContentType

from tags.models import TagItem

register = Library()

@register.filter
def get_tags(obj):
    dynamic_type = ContentType.objects.get_for_model(obj)

    items = TagItem.objects.filter(
        content_type=dynamic_type,
        object_id=obj.id,
        )

    return [item.tag for item in items]

@register.assignment_tag
def tags_cloud():
    
    tags = TagItem.objects.top_tags(20)
    
    return tags