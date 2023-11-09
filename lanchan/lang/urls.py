from django.urls import path
from lang import views

urlpatterns = [
    path('', views.main, name='main'), 
]
