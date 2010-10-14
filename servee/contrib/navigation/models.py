from django.db import models
from treebeard.ns_tree import NS_Node, NS_NodeManager
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class MenuItemManager(NS_NodeManager):
    """
    Works with multi-site configuration
    """
    def get_query_set(self, *args, **kwargs):
        return super(MenuItemManager, self).get_query_set(*args, **kwargs).filter(site=settings.SITE_ID)

# Create your models here.
class MenuItem(NS_Node):
    title      = models.CharField(max_length=255)
    urlpath    = models.CharField(max_length=255, blank=True, db_index=True)
    site       = models.ForeignKey(Site, related_name="sitepages", default=settings.SITE_ID)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.IntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    
    objects = MenuItemManager()
    
    def __unicode__(self):
        return u'%s' %(self.title)
        
    def __str__ (self):
        return u'%s' %(self.title)
            
    class Meta:
        # From treebeard docs
        #
        # Warning::
        #
        #  Be very careful if you add a Meta class in your
        #  ns_tree.NS_Node subclass. You must add an ordering
        #  attribute with two elements on it:
        #
        # class Meta:
        #     ordering = ['tree_id', 'lft']
        #
        # If you don't, the tree won't work, since ns_tree.NS_Node
        # completely depends on this attribute.
        
        #unique_together = (("urlpath", "site"),)
        ordering = ['tree_id', 'lft']
