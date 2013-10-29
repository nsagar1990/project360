from django.db import models

# Create your models here.

class Movie(models.Model):
	id			= models.AutoField(primary_key=True)
	movie_id 		= models.CharField(max_length=10)
	movie_name		= models.CharField(max_length=30)
	sub_title		= models.CharField(max_length=100)
	casting			= models.TextField() 
	director		= models.CharField(max_length=20)
	producer		= models.CharField(max_length=20)
	image_link		= models.CharField(max_length=255)
	genre			= models.CharField(max_length=50)
	plot 			= models.TextField()
	rating			= models.IntegerField()
	base_popularity		= models.IntegerField()
	release_date		= models.DateField()
	total_duration		= models.CharField(max_length=10)
	other_websites_rating	= models.CharField(max_length=10)
	wikipedia_link		= models.CharField(max_length=255)
	budget 			= models.CharField(max_length=50)
	created_at		= models.DateField()
	modifed_at		= models.DateField()

class Reviews(models.Model):
	id		= models.AutoField(primary_key=True)
	movie_id	= models.ForeignKey('Movie') 
	review_text	= models.TextField()
	rating 		= models.IntegerField()
	created_at	= models.DateField()
	modified_at	= models.DateField()

class Technicians(models.Model):
	id		= models.AutoField(primary_key=True)
	movie_id	= models.ForeignKey('Movie')
	cinematogapy	= models.CharField(max_length=50)
	stunt		= models.CharField(max_length=50)
	choregrahpy	= models.CharField(max_length=50)
	art_director 	= models.CharField(max_length=50)
	created_at      = models.DateField()
	modified_at     = models.DateField()


class News(models.Model):
    id              =  models.AutoField(primary_key=True)
    title           =  models.TextField()
    image_link      =  models.CharField(max_length=255)
    text            =  models.TextField()
    date            =  models.DateField()
    created_at      =  models.DateField()
    modifed_at      =  models.DateField()
