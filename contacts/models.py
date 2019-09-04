from django.db import models
from myApp.models import Home
# Create your models here.
##############################################CONTACT MODEL ############################################################
class Contact(models.Model):
    listing = models.CharField(max_length = 120)
    listing_id = models.IntegerField()
    name  = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)
    message = models.TextField(blank=True)
    date   = models.DateTimeField(auto_now_add=True,blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
