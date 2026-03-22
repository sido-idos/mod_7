from django import forms
from .models import Usuario, Operacion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = '__all__'