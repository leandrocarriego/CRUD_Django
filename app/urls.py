from django.urls import path
from .views import home, crear_disco, borrar_disco, editar_disco

urlpatterns = [
    path('', home),
    path('crear/', crear_disco, name="crear"),
    path("borrar/<int:disco_id>/", borrar_disco, name="borrar"),
    path("editar/<int:disco_id>/", editar_disco, name="editar")
]