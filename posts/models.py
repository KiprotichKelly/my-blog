from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(max_length=10000000)
    created_at =models.DateTimeField(default=datetime.now, blank=True)

class Meta:
    ordering = ['-created_at']

def __str__(self):
    return self.title    

