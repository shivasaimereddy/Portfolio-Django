from django.db import models
from datetime import datetime

# Create your models here.


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.summary
