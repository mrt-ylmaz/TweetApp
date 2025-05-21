from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    massege = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"Nick: {self.username}, Tweet= {self.massege}"
    #databasede nasıl gösterim sağlayacak
    