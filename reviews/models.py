from django.db import models
from django.db import models
from list.models import Tovar
from django.contrib.auth.models import User


class Review(models.Model):
    name = models.CharField(max_length=20)
    review = models.TextField(max_length=350)

class Comment(models.Model):
    review = models.TextField(max_length=350)
    product = models.ForeignKey(Tovar, on_delete= models.CASCADE, related_name= 'comments')
    name = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'user_name')