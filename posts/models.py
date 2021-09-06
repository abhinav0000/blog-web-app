from django.db import models
from datetime import datetime       #will help to save the date when a particular blog was created
# Create your models here.
class posts(models.Model):
    title= models.CharField(max_length=100)
    body= models.CharField(max_length=100000000000)
    created_at= models.DateTimeField(default=datetime.now,blank=True)