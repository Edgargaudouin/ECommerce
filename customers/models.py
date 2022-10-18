from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    address = models.CharField(max_lenght=200)
    contact = models.IntegerField()

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField(max_length=350, null=True, blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.FloatField()
    status = models.BooleanField(default=False)


    