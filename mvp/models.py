from django.db import models

class customer(models.Model):
    taskid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=245)
    phone = models.CharField(max_length=13)
    zip = models.CharField(max_length=5)
    task = models.CharField(max_length=100)
    description = models.TextField()

    
