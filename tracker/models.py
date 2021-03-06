from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	title        = models.CharField(max_length=200)
	description  = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	owner        = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.title


class Tracker(models.Model):
	# project     = models.ForeignKey(Project,on_delete=models.CASCADE)
	title       = models.CharField(max_length=200)
	description = models.TextField()
	# resolved    = models.BooleanField(default=False)


	def __str__(self):
		return self.title
