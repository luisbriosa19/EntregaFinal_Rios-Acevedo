from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#formularios creados. 

class CamisasFutbolFormulario(forms.Form):
    equipo=forms.CharField(max_length=60)
    marca=forms.CharField(max_length=60)
    año=forms.IntegerField()
    valoracion=forms.IntegerField()
    reseña=forms.CharField(widget=forms.Textarea)
    imagen=forms.ImageField()


class RegistrarseFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña Creada:", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"] 


class EditarFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la Contraseña Creada:", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"] 