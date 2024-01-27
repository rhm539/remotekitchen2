#urls.py
from django.urls import path
from . import views

urlpatterns = [
    #path('home/', HomePageView.as_view(), name='home'),
    #path('home/', views.home, name='home'),
    path('',  views.home, name='home'),
    
]