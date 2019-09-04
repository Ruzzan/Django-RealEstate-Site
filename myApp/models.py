from django.db import models
from realtors.models import Realtor
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class HomeManager(models.Manager):
    def get_queryset(self):
        return super(HomeManager, self).get_queryset().filter(status = 'published')

class Home(models.Model):
    # managers
    objects = models.Manager()
    homes = HomeManager()
    realtor  = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    slug     = models.SlugField(max_length=120, blank=True, null=True)
    #content of a house ad 
    title    = models.CharField(max_length = 120)
    address  = models.CharField(max_length = 100)
    city     = models.CharField(max_length = 200)
    district = models.CharField(max_length = 200)
    description = models.TextField(blank=True)
    price    = models.IntegerField()
    bedroom  = models.IntegerField()
    garage   = models.IntegerField(default=0)
    bathroom = models.IntegerField()
    sqft     = models.IntegerField()
    
    #images 
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)
    photo6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/',blank=True)

    # published or not 
    CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    ) 
    status = models.CharField(max_length = 100, choices = CHOICE, default = 'draft')

    # is_published = models.BooleanField(default=False)

    list_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail",args=[self.id])


############ slug ##############
@receiver(pre_save, sender=Home)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug
    





    
