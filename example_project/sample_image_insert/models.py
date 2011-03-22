from django.db import models
from django.conf import settings


class Image(models.Model):
    """
    Image model, really just a default, a more reasonable one
    would create some thumbnails based on the need of the site.
    """
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images")
    description = models.TextField(blank=True, null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s' % self.title
        
    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.image.name
        super(Image, self).save(*args, **kwargs) # Call the "real" save() method.

    @property
    def url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)

    class Meta:
        verbose_name = "basic image"
        verbose_name_plural = "basic images"
        ordering = ['-modified',]