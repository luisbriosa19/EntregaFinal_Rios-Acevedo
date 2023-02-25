from django.urls import path
from AppFinal.views import * 
from django.contrib.auth.views import LogoutView


#urls de nuestra aplicacion por cada vista creada.
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("iniciar_sesion/", iniciar_sesion, name = "iniciar_sesion"),
    path("registrarse/", registrarse, name = "registrarse"),
    path("editar_usuario/", editar_usuario, name = "editar_usuario"),
    path("cerrar_sesion/", LogoutView.as_view(template_name="AppFinal/cerrarsesion.html"), name="cerrar_sesion"),
    

    #CRUD
    path("ver_reseñas/", ver_reseñas, name= "ver_reseñas"),
    path("reseñacamisas/", crear_camisas, name="reseñascamisas"),
    path("editar_reseñas/<camisa_equipo>/", editar_reseñas, name= "editar_reseñas"),
    path("eliminar_reseñas/<camisa_equipo>/", eliminar_reseña, name= "eliminar_reseñas"),
    path("resultado_reseña/", resultado_reseña, name="resultado_reseña"),  
    ]

