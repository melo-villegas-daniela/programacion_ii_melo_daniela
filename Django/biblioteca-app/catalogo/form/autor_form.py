from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from catalogo.models import Libro, Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellido', 'nacionalidad']
    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellido': forms.Select(attrs={'class': 'form-control'}),
        'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),   
    }

    