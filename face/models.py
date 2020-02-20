from django.db import models
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.
class Opencv(models.Model):
	title = models.CharField(max_length=200)
	file_input = models.ImageField(upload_to='images/', blank=True)
	file_output = models.ImageField(blank=True)