from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# from reviews.models import Comment

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    def __str__(self) -> str:
        return f'{self.title}'
class Tovar(models.Model):

    title = models.CharField(max_length = 50)
    rating = models.IntegerField(default = 1, validators = [MaxValueValidator(5), MinValueValidator(1)])
    price = models.DecimalField(max_digits = 4, decimal_places = 2)     
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = True)
    # comments = models.ForeignKey(Comment)
    def __str__(self) -> str:
        return f'Товар {self.title}'
    def get_absolute_url(self):
        return reverse('product_detail', args= [self.id])
class Zakazi(models.Model):
    price=models.FloatField()

    
    
    