from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.favoritos,name="favoritos"),
    path('/apagar/<int:id>',views.apagar,name="apagar"),
]
