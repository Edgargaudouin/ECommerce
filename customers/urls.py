from django.urls import path
from customers.views import *


urlpatterns = [
    path('seeProducts/', seeProducts , name='seeProducts'),
]
