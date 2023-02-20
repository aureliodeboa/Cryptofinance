from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.plataforma,name="plataforma"),
    path('carteira',include('portifolio.urls'))
]
