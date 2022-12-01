from pyexpat import model
from tokenize import Name
from django.db import models
import uuid


# question for phase 1 
class share(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    Gender = [
        ('M','male'),
        ('F','Female')

    ]
    Options = [
        ('Y','yes'),
        ('N','no')
    ]
    
    gender = models.CharField(max_length=1,choices=Gender)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    Location = models.CharField(blank=False,max_length=100)
    Privacy= models.CharField(max_length=1,choices=Options)
    Story = models.TextField(blank=False)
    Comtot = models.IntegerField(default=0,null=True,blank=True)
    
    def __str__(self):
        return self.Name

class comment(models.Model):
    
    comment = models.CharField(max_length=30)
    share = models.ForeignKey(share,on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return self.Title