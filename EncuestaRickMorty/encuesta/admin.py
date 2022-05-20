from django.contrib import admin
from .models import Opcion, Pregunta


class OpcionInLine(admin.TabularInline):
    model = Opcion
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    fields = ["pregunta_texto"]
    inlines = [OpcionInLine]

    # Campos que se muestran en el entorno gráfico
    list_display = ["pregunta_texto", "id", "fecha_publicacion"]
    # Agrefamos una barra de filtración

    list_filter = ["fecha_publicacion"]
    
    # Agregamos una barra de busqueda sobre un campo
    search_fields = ["pregunta_texto"]


admin.site.register(Pregunta, PreguntaAdmin)
