from django.db import models

# Create your models here.
class Genero(models.Model):

    nombre_genero = models.CharField(unique=True)

    def __str__(self):
        return self.nombre_genero

class Pelicula(models.Model):

    nombre_pelicula = models.CharField(unique=True)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='media/', blank=True, null=True)
    precio_entrada = models.PositiveSmallIntegerField()
    en_cartelera = models.BooleanField()

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="generos",)

    def __str__(self):
        return self.nombre_pelicula

class Ticket(models.Model):

    cliente = models.CharField(unique=True)
    correo = models.EmailField(blank=True)
    entradas = models.PositiveBigIntegerField(default=1)
    compra = models.DateTimeField(auto_now_add=True)
    codigo = models.PositiveIntegerField(unique=True)

    ticket_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name="peliculas",)

    def __str__(self):
        return self.cliente