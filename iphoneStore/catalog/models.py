from django.db import models
from django.urls import reverse

# Create your models here.
class Items(models.Model):
   
    title = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos") #photos/%y/%m/%d/ сортування фото по даті створення
    memoryGB = models.IntegerField(blank=True)
    screen_diagonal = models.FloatField()   
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT) #індифікатор категорії    Category в лапках бо клас створений нижче
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_page', kwargs={'item_id':self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_filter', kwargs={'cat_id':self.pk})