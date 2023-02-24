from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.plataforma,name="plataforma"),
    path('mercado',views.mercado,name="mercado"),
    path('carteira',include('portifolio.urls')),
    path('favoritos',include('favoritos.urls')),

]
