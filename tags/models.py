# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.urlresolvers import reverse
from django.db.models import Count


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_name': self.name})


class TagManager(models.Manager):
    def top_tags(self, max=15):
        top = self.model.objects.values(
                  'tag__name').annotate(
                      score=Count('tag')).order_by('-score')[:max]

        return top


class TagItem(models.Model):
    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')

    tag = models.ForeignKey('Tag')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    obj = GenericForeignKey('content_type', 'object_id')

    objects = TagManager()
