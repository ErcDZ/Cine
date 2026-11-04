from django.contrib import admin
from django.utils.html import format_html
from .models import Genero, Pelicula, Ticket

# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ["nombre_genero"]

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ["nombre_pelicula", "imagen", "en_cartelera", "precio_entrada"]
    readonly_fields = ('miniatura',)
    fields = ('nombre_pelicula', 'imagen', 'miniatura')

    @admin.display(description='Vista previa')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;">'
            )

        return '-'


admin.site.register(Genero)
admin.site.register(Pelicula)