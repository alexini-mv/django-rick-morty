from django.urls import path

from . import views

app_name = "encuesta"

urlpatterns = [
    # Ejemplo de la ruta: /encuesta/
    path('/', views.IndexView.as_view(), name='index'),
    # Ejemplo de la ruta: /encuesta/detalle/5/
    path('/detalle/<int:pk>/', views.DetalleView.as_view(), name='detalle'),
    # Ejemplo de la ruta: /encuesta/resultado/5
    path('/resultado/<int:pk>/', views.ResultadoView.as_view(), name='resultado'),
    # Ejemplo de la ruta: /encuesta/votos/5
    path('/votos/<int:pk>/', views.ResultadoView.as_view(), name='voto')
]
