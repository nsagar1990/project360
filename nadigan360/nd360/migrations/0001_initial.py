# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'nd360_movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('movie_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sub_title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('casting', self.gf('django.db.models.fields.TextField')()),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('producer', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('image_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('plot', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('base_popularity', self.gf('django.db.models.fields.IntegerField')()),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('total_duration', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('other_websites_rating', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('wikipedia_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('budget', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('modifed_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'nd360', ['Movie'])

        # Adding model 'Reviews'
        db.create_table(u'nd360_reviews', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('review_text', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('modified_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'nd360', ['Reviews'])

        # Adding model 'Technicians'
        db.create_table(u'nd360_technicians', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movie_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nd360.Movie'])),
            ('cinematogapy', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('stunt', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('choregrahpy', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('art_director', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('modified_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'nd360', ['Technicians'])

        # Adding model 'News'
        db.create_table(u'nd360_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('dis_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image_link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('created_at', self.gf('django.db.models.fields.DateField')()),
            ('modifed_at', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'nd360', ['News'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'nd360_movie')

        # Deleting model 'Reviews'
        db.delete_table(u'nd360_reviews')

        # Deleting model 'Technicians'
        db.delete_table(u'nd360_technicians')

        # Deleting model 'News'
        db.delete_table(u'nd360_news')


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
            'dis_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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