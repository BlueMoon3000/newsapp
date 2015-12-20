# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AppUser'
        db.create_table(u'core_appuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('fb_user_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fb_access_token', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['AppUser'])

        # Adding model 'Topic'
        db.create_table(u'core_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('last_updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Topic'])

        # Adding model 'SearchTopic'
        db.create_table(u'core_searchtopic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Topic'])),
            ('is_master', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['SearchTopic'])

        # Adding model 'Article'
        db.create_table(u'core_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('last_updated_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Article'])


    def backwards(self, orm):
        # Deleting model 'AppUser'
        db.delete_table(u'core_appuser')

        # Deleting model 'Topic'
        db.delete_table(u'core_topic')

        # Deleting model 'SearchTopic'
        db.delete_table(u'core_searchtopic')

        # Deleting model 'Article'
        db.delete_table(u'core_article')


    models = {
        u'core.appuser': {
            'Meta': {'object_name': 'AppUser'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'fb_access_token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'fb_user_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'last_updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'core.article': {
            'Meta': {'object_name': 'Article'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        },
        u'core.searchtopic': {
            'Meta': {'object_name': 'SearchTopic'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Topic']"})
        },
        u'core.topic': {
            'Meta': {'object_name': 'Topic'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['core']