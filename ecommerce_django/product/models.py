from io import BytesIO
from unicodedata import category
from PIL import Image

from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField()

  class Meta:
    ordering = ('name',)

  def __str__(self):
    return  self.name

  def get_absolute_url(self):
    return f'/{self.slug}/'

class Product(models.Model):
  # Add ForeignKey to Product based on Cate, on delete will remove, products is the calling name, categories.products etc
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)