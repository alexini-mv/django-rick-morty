from django.db import models


class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)


class Opcion(models.Model):
    pregunta_id = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)