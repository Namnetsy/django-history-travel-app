from django.db import models
from froala_editor.fields import FroalaField

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images')
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	text = FroalaField()
	published_date = models.DateTimeField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return  '/post/' + str(self.pk) + '/'

	class Meta:
		verbose_name = 'стаття'
		verbose_name_plural = 'статті'

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'категорія'
		verbose_name_plural = 'категорії'
