from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['prénom', 'nom', 'email', 'nombre_de_places','age']
         
