# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Registration.nr1'
        db.add_column(u'website_registration', 'nr1',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Registration.nr2'
        db.add_column(u'website_registration', 'nr2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Registration.nr3'
        db.add_column(u'website_registration', 'nr3',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Registration.nr1'
        db.delete_column(u'website_registration', 'nr1')

        # Deleting field 'Registration.nr2'
        db.delete_column(u'website_registration', 'nr2')

        # Deleting field 'Registration.nr3'
        db.delete_column(u'website_registration', 'nr3')


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
            'research': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'special_needs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'university': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['website']