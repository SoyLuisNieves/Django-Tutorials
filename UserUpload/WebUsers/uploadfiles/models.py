from django.db import models

# Create your models here.
from django.core.urlresolvers import reverse

class User(models.Model):
	username = models.CharField(max_length=50)
	user_avatar = models.FileField()

	def get_absolute_url(self):
		return reverse('uploadfiles:home')