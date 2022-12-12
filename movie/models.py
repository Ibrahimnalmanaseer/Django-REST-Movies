from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Movie(models.Model):

    title=models.CharField(max_length=50,default='movie')
    desc=models.TextField()
    rate=models.FloatField()
    type=models.TextField()
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default=1)
    
