from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=25,blank=False)
    id=models.IntegerField(primary_key=True)
    price=models.IntegerField()

    def __str__(self):
        return self.name
    