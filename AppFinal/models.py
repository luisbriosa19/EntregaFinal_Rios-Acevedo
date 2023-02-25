from django.db import models

# Create your models here.
#modelos usados en el proyecto. 

class Camisa_Futbol(models.Model):

    def __str__(self):
        return f"Equipo: {self.equipo} - Marca: {self.marca} - año: {self.año} - Valoracion:{self.valoracion}"
    
    equipo=models.CharField(max_length=60)
    marca=models.CharField(max_length=60)
    año=models.IntegerField()
    valoracion=models.IntegerField()
    reseña=models.TextField(max_length=240)
    imagen=models.ImageField(upload_to = "camisas", null=True, blank=True)


