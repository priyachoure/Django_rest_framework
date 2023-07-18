from django.db import models


# Create your models here.
class movies(models.Model):
    name = models.CharField(max_length=100)
    Discription = models.TextField(max_length=100)
    Active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
