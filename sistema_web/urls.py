from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('plataforma/', include('plataforma.urls')),
    
    path('',views.inicial,name="inicial"),
  
]
