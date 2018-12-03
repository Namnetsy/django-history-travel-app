from django.db import models

class Folk(models.Model):
	instance_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='images')

	def __str__(self):
		return self.instance_user.username
