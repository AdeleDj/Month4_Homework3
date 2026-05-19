from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    genre = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='covers/')
    created_at = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='books/', null=True, blank=True)
    views = models.IntegerField(default=0)
