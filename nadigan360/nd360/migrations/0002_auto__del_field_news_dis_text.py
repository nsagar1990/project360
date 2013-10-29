# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'News.dis_text'
        db.delete_column(u'nd360_news', 'dis_text')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'News.dis_text'
        raise RuntimeError("Cannot reverse this migration. 'News.dis_text' and its values cannot be restored.")

    models = {
        u'nd360.movie': {
            'Meta': {'object_name': 'Movie'},
            'base_popularity': ('django.db.models.fields.IntegerField', [], {}),
            'budget': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'casting': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modifed_at': ('django.db.models.fields.DateField', [], {}),
            'movie_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'movie_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'other_websites_rating': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'plot': ('django.db.models.fields.TextField', [], {}),
            'producer': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_duration': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'wikipedia_link': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'nd360.news': {
            'Meta': {'object_name': 'News'},
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modifed_at': ('django.db.models.fields.DateField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'nd360.reviews': {
            'Meta': {'object_name': 'Reviews'},
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'review_text': ('django.db.models.fields.TextField', [], {})
        },
        u'nd360.technicians': {
            'Meta': {'object_name': 'Technicians'},
            'art_director': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'choregrahpy': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cinematogapy': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created_at': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateField', [], {}),
            'movie_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nd360.Movie']"}),
            'stunt': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['nd360']