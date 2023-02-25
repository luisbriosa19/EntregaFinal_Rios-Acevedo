from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from AppFinal.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
#Vista para poder iniciar sesion. 
def iniciar_sesion(request):  #al presionar el botón "Iniciar Sesión"
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión
        if form.is_valid():
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contraseña=form.cleaned_data.get('password')    #leer la contraseña ingresada
            user=authenticate(username=usuario, password=contraseña)    #buscar al usuario con los datos ingresados

            if user:    #si ha encontrado un usuario con eso datos
                login(request, user)   #hacemos login
                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "AppFinal/inicio.html", {'mensaje':f"Bienvenido a la pagina {user}"}) 
        else:   #si el formulario no es valido (no encuentra usuario)
        #mostramos la página de inicio junto a un mensaje de error.
            return render(request, "AppFinal/inicio.html", {'mensaje':"Error. Datos ingresados son incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "AppFinal/iniciarsesion.html", {"formulario":form})

#Vista para registrarse
def registrarse(request):
    if request.method == 'POST':    #cuando le haga click al botón
        form = RegistrarseFormulario(request.POST)   #leer los datos   llenados en el formulario
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()
            return render(request, "AppFinal/inicio.html", {'mensaje':"Usuario Creado con Exito"})
    else:
        form = RegistrarseFormulario()   #formulario de django que nos permite crear usuarios.
    return render(request, "AppFinal/registrarse.html", {"formulario":form})

#Vista para Editar Usuarios resistrados.
@login_required
def editar_usuario(request):
    usuario = request.user #usuario activo (el que ha iniciado sesión)
    if request.method == "POST":    #al presionar el botón
        form = EditarFormulario(request.POST) #el formulario es el del usuario
        if form.is_valid():
            info = form.cleaned_data     #info en modo diccionario
            #actualizar la info del usuario activo
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.email = info["email"]
            usuario.set_password1 = info["password1"]
            usuario.password2 = info["password1"]
            usuario.save()
            return render(request, "AppFinal/inicio.html")
    else:
        form= EditarFormulario(initial={"email":usuario.email, "first_name":usuario.first_name, "last_name":usuario.last_name,})
    return render(request, "AppFinal/editarusuario.html",{"formulario":form, "usuario":usuario})


def inicio(request):
    return render(request,"AppFinal\inicio.html")

@login_required
def crear_camisas(request): #formulario carga de datos del models Jugadores
    if request.method == 'POST': # al hacer click a enviar: se van a guardar los datos y crearse el curso en la BD.
        form_Camisas = CamisasFutbolFormulario(request.POST, request.FILES)
        if form_Camisas.is_valid(): #validacion de datos
            Camisasdicc = form_Camisas.cleaned_data #convertir la informacion a informacion tipo diccionario.
            camisa1 = Camisa_Futbol(equipo = Camisasdicc["equipo"], marca = Camisasdicc["marca"], año = Camisasdicc["año"], valoracion = Camisasdicc["valoracion"], reseña = Camisasdicc["reseña"], imagen = Camisasdicc["imagen"], )
            camisa1.save() #guardamos la informacion del diccionario.
            return render(request, "AppFinal/Inicio.html") #Vinculo a la pagina de Inicio de nuestro template.
    else: #si no le doy click en enviar debo mostrar el formulario vacio
        form_Camisas = CamisasFutbolFormulario()
    return render(request, "AppFinal/reseñacamisas.html", {"formcamisas1":form_Camisas})

@login_required
def ver_reseñas(request):
    camisas = Camisa_Futbol.objects.all().order_by('-valoracion')
    return render(request, "AppFinal/listadoreseñas.html",{'Camisas': camisas})

@login_required
def editar_reseñas(request, camisa_equipo):
    Camisa = Camisa_Futbol.objects.get(equipo=camisa_equipo)
    if request.method == "POST":
        form_Camisas = CamisasFutbolFormulario(request.POST, request.FILES)
        if form_Camisas.is_valid():
            Camisasdicc = form_Camisas.cleaned_data
            Camisa.equipo = Camisasdicc['equipo']
            Camisa.marca = Camisasdicc['marca']
            Camisa.año = Camisasdicc['año']
            Camisa.valoracion = Camisasdicc['valoracion']
            Camisa.reseña = Camisasdicc['reseña']
            Camisa.imagen = Camisasdicc['imagen']
            Camisa.save()
            return render(request, "AppFinal/inicio.html")
    else:
        form_Camisas = CamisasFutbolFormulario(initial={'equipo':Camisa.equipo, 'marca':Camisa.marca,
        'año':Camisa.año, 'valoracion':Camisa.valoracion, 'reseña':Camisa.reseña, 'imagen':Camisa.imagen})
    return render(request, "AppFinal/editarreseñas.html",{'formcamisas1':form_Camisas, 'equipo':camisa_equipo})

@login_required
def eliminar_reseña(request, camisa_equipo):
    Camisa = Camisa_Futbol.objects.get(equipo=camisa_equipo)
    Camisa.delete()
    camisas = Camisa_Futbol.objects.all().order_by('-valoracion')
    return render(request, "AppFinal/listadoreseñas.html",{'Camisas': camisas})

def busqueda_reseña(request):
    return render(request, "AppFinal/inicio.html")

#Vista de resultados de datos solicitados.
def resultado_reseña(request):
    if request.GET["equipo"]:
        equipo = request.GET["equipo"]
        camisas = Camisa_Futbol.objects.filter(equipo__icontains=equipo)
        return render(request, "AppFinal/inicio.html", {"camisas":camisas, "equipo":equipo}) 
    else:
        respuesta = "No enviaste datos."
    return HttpResponse(respuesta)


