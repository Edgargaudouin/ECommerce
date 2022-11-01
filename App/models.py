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
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name + " --- $" + str(self.price) 

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    address = models.CharField(max_length=200,default='', blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    delivey_time = models.DateTimeField()
    

    def get_order_id(self):
        return "Order" + str(self.id)

    def get_total_price(self):
        return sum(item.get_price() for item in self.items.all())

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    price = models.FloatField()
    quantity = models.FloatField()

    def get_price(self):
        return self.price * self.quantity