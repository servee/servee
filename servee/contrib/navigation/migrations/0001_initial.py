# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'MenuItem'
        db.create_table('navigation_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('rgt', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('depth', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('urlpath', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='sitepages', to=orm['sites.Site'])),
        ))
        db.send_create_signal('navigation', ['MenuItem'])

        # Adding unique constraint on 'MenuItem', fields ['urlpath', 'site']
        db.create_unique('navigation_menuitem', ['urlpath', 'site_id'])


    def backwards(self, orm):
        
        # Deleting model 'MenuItem'
        db.delete_table('navigation_menuitem')

        # Removing unique constraint on 'MenuItem', fields ['urlpath', 'site']
        db.delete_unique('navigation_menuitem', ['urlpath', 'site_id'])


    models = {
        'navigation.menuitem': {
            'Meta': {'unique_together': "(('urlpath', 'site'),)", 'object_name': 'MenuItem'},
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'rgt': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'sitepages'", 'to': "orm['sites.Site']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'urlpath': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['navigation']
