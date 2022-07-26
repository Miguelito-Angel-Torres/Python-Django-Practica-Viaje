from django import forms
from django.forms.widgets import Textarea

class FormularioContacto(forms.Form):
    nombre =forms.CharField(label='Nombre:',required=True,)
    apellido=forms.CharField(label='Apellido:',required=True)
    email = forms.CharField(label='Email:',required=True)
    contenido= forms.CharField(label='Mensaje:',required=True,widget=forms.Textarea())
   