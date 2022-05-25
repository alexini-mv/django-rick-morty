from django.shortcuts import render, get_object_or_404

# Construiremos un BodyResponse de una petición
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.views import generic

from .models import Pregunta, Opcion


# GENERIC VIEWS (Class Based Views)

class IndexView(generic.ListView):
    template_name = "encuesta/index.html"
    context_object_name = "lista_de_preguntas"


class DetalleView(generic.DetailView):
    model = Pregunta
    template_name = "encuesta/detalle.html"


class ResultadoView(generic.DetailView):
    model = Pregunta
    template_name = "encuesta/resultado.html"


def voto(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, pk=pregunta_id)

    try:
        opcion_selecionada = pregunta.pregunta_set.get(
            pk=request.POST["choice"])

    except (KeyError, Opcion.DoesNotExist):
        return render(request=request,
                      template_name="encuesta/detalle.html",
                      context={
                          "pregunta": pregunta,
                          "error_message": "¡No elegiste una respuesta!"
                      })

    else:
        opcion_selecionada.votes += 1
        opcion_selecionada.save()

        return HttpResponseRedirect(reverse("encuesta:resultado", args=(pregunta_id,)))


# FUNCTION BASED VIEWS:
# Definimos la respuesta del request

# def index(request):
#     return render(request=request,
#                   template_name="encuesta/index.html",
#                   context={
#                       "lista_de_preguntas": Pregunta.objects.all()
#                   }
#                   )


# def details(request, pregunta_id):
#     pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
#     return render(request=request,
#                   template_name="encuesta/detalle.html",
#                   context={
#                       "pregunta": pregunta
#                   })


# def results(request, pregunta_id):
#     pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
#     return render(request=request,
#                   template_name="encuesta/resultado.html",
#                   context={
#                       "pregunta": pregunta
#                   })
