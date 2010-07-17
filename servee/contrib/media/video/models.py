from django.db import models
from tagging.fields import TagField
from django.conf import settings

import tagging

class Video(models.Model):
    """Video model"""
    title = models.CharField(max_length=255, blank=True, null=True)
    still = models.ImageField(upload_to="videos/stills")
    video = models.FileField(upload_to="videos")
    description = models.TextField(blank=True, null=True)
    tags = TagField()
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.title
        
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.video.name
        super(Image, self).save(*args, **kwargs) # Call the "real" save() method.

    @property
    def url(self):
        return '%s%s' % (settings.MEDIA_URL, self.video)

    class Meta:
        ordering = ['modified',]