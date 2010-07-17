from django.db import models
from tagging.fields import TagField
from django.conf import settings

import tagging

class Document(models.Model):
    """Document model"""
    title = models.CharField(max_length=255, blank=True, null=True)
    document = models.FileField(upload_to="documents")
    description = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    tags = TagField()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.title
        
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.document.name
        super(Document, self).save(*args, **kwargs) # Call the "real" save() method.

    @property
    def url(self):
        return '%s%s' % (settings.MEDIA_URL, self.document)

    class Meta:
        ordering = ['modified',]