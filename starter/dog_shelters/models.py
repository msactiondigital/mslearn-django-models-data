from django.db import models
class Product(models.Model):
    name = models.TextField()
    price = models.DecimalField()
    creation_date = models.DateField()
    category = models.ForeignKey(
        'Category', #The name of the model
        on_delete=models.PROTECT
    )
    

class Category(models.Model):
    name = models.TextField()
    # product_set will be automatically created