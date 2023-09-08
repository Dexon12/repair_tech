from django.db import models
from django.urls import reverse
from django.db.models import Q
from fuzzywuzzy import fuzz


class Services(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/1")
    second_photo = models.ImageField(upload_to="photos/%Y/%m/%d/2",blank=True, null=True)
    third_photo = models.ImageField(upload_to="photos/%Y/%m/%d/3",blank=True, null=True) 
    forth_photo = models.ImageField(upload_to="photos/%Y/%m/%d/4",blank=True, null=True) 
    fifth_photo = models.ImageField(upload_to="photos/%Y/%m/%d/5",blank=True, null=True) 
    sixth_photo = models.ImageField(upload_to="photos/%Y/%m/%d/6",blank=True, null=True) 
    discripts = models.CharField(max_length=1800, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service', kwargs={"service_slug": self.slug})
    
