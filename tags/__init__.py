from models import Tag, TagItem
from django.contrib.contenttypes.models import ContentType

def set_tags(obj, tags):
    dynamic_type = ContentType.objects.get_for_model(obj)

    TagItem.objects.filter(
        content_type=dynamic_type,
        object_id=obj.id,
        ).delete()

    tags = tags.split(' ')
    for tag_name in tags:
        tag, is_new = Tag.objects.get_or_create(name=tag_name.strip())

        TagItem.objects.get_or_create(
            tag=tag,
            content_type=dynamic_type,
            object_id=obj.id,
        )

def get_tags(obj):
    dynamic_type = ContentType.objects.get_for_model(obj)

    tags = TagItem.objects.filter(
        content_type=dynamic_type,
        object_id=obj.id,
        )
    
    return ' '.join([item.tag.name for item in tags])