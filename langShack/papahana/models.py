#from nltk import *
from django.db import models
from django.utils import timezone

# Create your models here.
class Workbench(models.Model):
    created_date = models.DateTimeField(
        default=timezone.now)
    pattern = models.TextField()
