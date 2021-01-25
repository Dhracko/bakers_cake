""" Define the mapping between URLs and views """


from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_news, name='newsletter'),
    path('', views.index, name='home'),
]
