#from nltk import *
from django.db import models
from django.utils import timezone

# Create your models here.
class Workbench(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    description = models.TextField()
    pattern = models.CharField(max_length=25, null=True)


class upLoad(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    document = models.FileField(default="d", upload_to='media/')
