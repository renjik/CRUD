from django.db import models

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=20)
    pdf = models.FileField(upload_to='pages/') 
    cover = models.FileField(upload_to='pics/') 
    