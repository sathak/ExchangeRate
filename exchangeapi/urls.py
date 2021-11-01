from django.contrib import admin
from django.urls import path
from .views import exchange_list 
 
urlpatterns = [ 
    
       path('v1/quotes',exchange_list),
]