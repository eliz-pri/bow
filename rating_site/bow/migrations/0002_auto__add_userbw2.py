# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserBW2'
        db.create_table(u'bow_userbw2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('btr_res', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('wrs_res', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bow', ['UserBW2'])


    def backwards(self, orm):
        # Deleting model 'UserBW2'
        db.delete_table(u'bow_userbw2')


    models = {
        u'bow.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'res_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bow.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bow.userbw': {
            'Meta': {'object_name': 'UserBW'},
            'btr_res': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'btr'", 'to': u"orm['bow.Restaurant']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wrs_res': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wrs'", 'to': u"orm['bow.Restaurant']"})
        },
        u'bow.userbw2': {
            'Meta': {'object_name': 'UserBW2'},
            'btr_res': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'wrs_res': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bow']