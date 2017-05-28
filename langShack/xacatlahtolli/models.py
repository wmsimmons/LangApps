from django.db import models

# Create your models here.
class Shack(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=175)
	description = models.TextField()


	def __str__(self):
		return self.title