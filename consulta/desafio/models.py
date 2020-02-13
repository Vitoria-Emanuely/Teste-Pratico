from django.db import models

class Dados(models.Model):
   data = models.DateField(null=True, blank=True)
   nota_fiscal = models.CharField(max_length=7)
   transportadora = models.CharField(max_length=20)
   placa = models.CharField(max_length=8)
 
   def __str__(self):
       return self.transportadora