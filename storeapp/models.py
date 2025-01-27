from django.db import models

# Create your models here.
class items (models.Model):
    itemname = models.CharField(max_length=50)
    itemprice = models.CharField(max_length=8)

    def __str__(self):
        return f'item Name : {self.itemname}, itemPrice : {self.itemprice}'