from django.db import models

# Create your models here.


class Room(models.model):
    # host = 
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField