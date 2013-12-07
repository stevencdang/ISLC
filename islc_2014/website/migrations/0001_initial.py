# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'website_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'website', ['Person'])

        # Adding model 'Address'
        db.create_table(u'website_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'website', ['Address'])

        # Adding model 'Email'
        db.create_table(u'website_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'website', ['Email'])

        # Adding model 'Phone'
        db.create_table(u'website_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('work', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'website', ['Phone'])

        # Adding model 'Registration'
        db.create_table(u'website_registration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=254, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('slc', self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True)),
            ('department', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True)),
            ('university', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('research', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('diet', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'website', ['Registration'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'website_person')

        # Deleting model 'Address'
        db.delete_table(u'website_address')

        # Deleting model 'Email'
        db.delete_table(u'website_email')

        # Deleting model 'Phone'
        db.delete_table(u'website_phone')

        # Deleting model 'Registration'
        db.delete_table(u'website_registration')


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
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'diet': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'research': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'slc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'university': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['website']