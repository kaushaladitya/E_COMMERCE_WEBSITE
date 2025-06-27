from django.db import models

# Create your models here.

class Product(models.Model):
    name =models.CharField(max_length=100)
    description = models.TextField()
    price =  models.IntegerField()

    #migration is used to create the table in the database


wild photographic link
couple wedding image link
laptop image link
image link

crete only varchar feild