from django.db import models
from froala_editor.fields import FroalaField

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	text = FroalaField()
	published_date = models.DateTimeField()

	def __str__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
