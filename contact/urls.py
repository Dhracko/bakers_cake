""" Define the mapping between URLs and views """

from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
]
