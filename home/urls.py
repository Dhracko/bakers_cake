""" URL for the functions """


from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_news, name='newsletter'),
    path('', views.index, name='home'),
]
