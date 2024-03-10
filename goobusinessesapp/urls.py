from django.contrib import admin
from django.urls import path
from goobusinessesapp import views

urlpatterns = [
    path("", views.index, name='home'),
    
    path("referral", views.referral, name="referral"),
    


    
]
