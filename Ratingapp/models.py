from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=40)
    Image = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.Name

class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    Title = models.CharField(max_length=30)
    Description = models.TextField()
    Model = models.CharField(max_length=40)
    Image = models.CharField(max_length=400)

    def __str__(self):
        return '{} model {}'.format(self.Title, self.Model)

class Ratings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.CharField(max_length=30)
    posted_on = models.DateTimeField(auto_now_add=True)