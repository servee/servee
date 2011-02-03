from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _


class Gallery(models.Model):
    """Gallery model"""
    title = models.CharField(verbose_name=_('title'), max_length=255, blank=True, null=True)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.title
        
class GalleryItem(models.Model):
    """
    Holds the relationship between a Gallery and the item inside.
    """
    gallery = models.ForeignKey(Gallery, verbose_name=_('gallery'), related_name='items')
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object id'), db_index=True)
    object = generic.GenericForeignKey('content_type', 'object_id')
    order = models.IntegerField(blank=True,null=True)

    class Meta:
        # Enforce unique association per object
        unique_together = (('gallery', 'content_type', 'object_id'),)
        verbose_name = _('gallery item')
        ordering = ('order',)
        verbose_name_plural = _('gallery items')

    def __unicode__(self):
        return u'%s [%s]' % (self.object, self.gallery)
        
class GalleryModel(models.Model):
    """
    Registered models that show up when building galleries
    """
    content_type = models.ForeignKey(ContentType)