from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    username=models.CharField(max_length=100, null = True)    
    title=models.CharField(max_length=100)
    description=models.TextField()
    complete=models.CharField(max_length=15, null = True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

        class Meta:
            ordering=['complete']

class Accounts(models.Model):
    username=models.CharField(max_length=100, null = True)    
    fullname=models.CharField(max_length=100)
    emailid=models.TextField()
    password=models.CharField(max_length=100, null = True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

        class Meta:
            ordering=['created']
