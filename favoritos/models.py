from django.db import models
from django.contrib.auth.models import User


class Favoritos(models.Model):
    usuario= models.ForeignKey(to=User, on_delete=models.CASCADE)
    moeda= models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.moeda)
   