from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('index/', views.index),
    path('insert/', views.insert),
    path('query/', views.query),
]
