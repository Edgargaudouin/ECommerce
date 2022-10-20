import email
from email.policy import default
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    adress = models.CharField(max_length=200, null=False, blank=False)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField()
    cost = models.FloatField()
    internalTax = models.FloatField(default=0) #Internal Tax for tabbacco products
    vat = models.FloatField(default=21) #Value added tax 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=350, default = '', blank=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name + " --- $" + str(self.price) 

class Order(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.FloatField()
    price = models.FloatField()
    address = models.CharField(max_length=200,default='', blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


    