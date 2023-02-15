from django.db import models

# Create your models here.
class Member (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name + ' ' + self.email + ' ' + self.contact