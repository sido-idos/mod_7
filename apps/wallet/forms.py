from django import forms
from .models import Usuario, Operacion

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-dark text-light'}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light'}),
        }

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = '__all__'
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-select bg-dark text-light'}),
            'tipo': forms.Select(attrs={'class': 'form-select bg-dark text-light'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control bg-dark text-light', 'type':'date'}),
        }