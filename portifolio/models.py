from django.db import models
from django.contrib.auth.models import User

class Carteira(models.Model):
    usuario= models.ForeignKey(to=User, on_delete=models.CASCADE)
    moeda= models.CharField(max_length=150)
    symbol = models.CharField(max_length=20,default=None)
    quantidade= models.CharField(max_length=50, default=None, null=True, blank=True)
    valordecompra= models.CharField(max_length=50, default=None, null=True, blank=True)
    def __str__(self):
        return str(self.moeda)

