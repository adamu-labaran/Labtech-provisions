# create url path for view functionality to see your view from the web
from django.urls import path

# importing views function
from . import views

# create url patterns to path index
urlpatterns = [
    path('', views.index, name='index'), # then go to urls.py in ecomerce and include the path
    path('about', views.about, name='about') # then go to urls.py in ecomerce and include the path
]