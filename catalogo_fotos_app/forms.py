from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from catalogo_fotos_app.models import *

# formulario carga album
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        exclude = []
        widgets = {
            "descripcion": forms.Textarea(attrs={"class": "materialize-textarea"}),
            # "titulo": forms.TextInput(
            #     attrs={"class": "vTextField", "id": "id_titulo titulo_copiar"}
            # ),
            # "slug": forms.TextInput(
            #     attrs={"class": "vTextField", "id": "id_slug slug_copiar"}
            # ),
            # "slug": forms.HiddenInput()
        }  # para que no se muestre en el formulario pero tampoco se muestra en admin. VER ESTO

    zip = forms.FileField(required=False)


# formulario registro users admin?
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=True,
        help_text="Ingresa tu nombre",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text="Ingresa tu apellido",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    username = forms.CharField(
        label="Usuario",
        max_length=30,
        required=True,
        help_text="Ingresa tu usuario",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        help_text="Ingresa tu email",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        help_text="Ingresa tu contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        label="Repetir contraseña",
        required=True,
        help_text="Repite tu contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    # check = forms.BooleanField(
    #     required=True,
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             "type": "checkbox",
    #         }
    #     ),
    # )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
        help_texts = {k: "" for k in fields}


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        label=("remember_me"), initial=False, required=False
    )


# formnulario de contacto
class Contactos(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"
        exclude = []
        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control input-field col s12", "id": "id_nombre"}
            ),
            "apellido": forms.TextInput(
                attrs={"class": "form-control input-field col s12", "id": "id_apellido"}
            ),
            "email": forms.TextInput(
                attrs={"class": "form-control input-field col s12", "id": "id_email"}
            ),
            "subject": forms.TextInput(
                attrs={"class": "form-control input-field col s12", "id": "id_subject"}
            ),
            "message": forms.Textarea(
                attrs={"class": "form-control input-field col s12", "id": "id_message"}
            ),
        }
