from django.db import models

# Create your models here.
class Topics(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
