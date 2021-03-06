# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Registration.abstract'
        db.add_column(u'website_registration', 'abstract',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)

        # Adding field 'Registration.symposium_talk'
        db.add_column(u'website_registration', 'symposium_talk',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Registration.children_museum'
        db.add_column(u'website_registration', 'children_museum',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Registration.child_museum_essay'
        db.add_column(u'website_registration', 'child_museum_essay',
                      self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Registration.abstract'
        db.delete_column(u'website_registration', 'abstract')

        # Deleting field 'Registration.symposium_talk'
        db.delete_column(u'website_registration', 'symposium_talk')

        # Deleting field 'Registration.children_museum'
        db.delete_column(u'website_registration', 'children_museum')

        # Deleting field 'Registration.child_museum_essay'
        db.delete_column(u'website_registration', 'child_museum_essay')


    models = {
        u'website.address': {
            'Meta': {'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'website.email': {
            'Meta': {'object_name': 'Email'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'website.person': {
            'Meta': {'object_name': 'Person'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'website.phone': {
            'Meta': {'object_name': 'Phone'},
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'website.registration': {
            'Meta': {'object_name': 'Registration'},
            'abstract': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'child_museum_essay': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'children_museum': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'diet': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'nr1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'nr2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'nr3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.FileField', [], {'default': "'default_face.jpg'", 'max_length': '100'}),
            'research': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'special_needs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'symposium_talk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'university': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['website']