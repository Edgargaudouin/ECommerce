from django.contrib import admin
from customers.models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Orders)