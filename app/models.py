from django.db import models

# Create your models here.
class Disco(models.Model):
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    estilo = models.CharField(max_length=50)
    
    