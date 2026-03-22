from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Operacion
from .forms import UsuarioForm, OperacionForm

# Create your views here.

# -------- USUARIOS --------
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'wallet/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'wallet/form_usuario.html', {'form': form})

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, 'wallet/form_usuario.html', {'form': form})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('lista_usuarios')


# -------- OPERACIONES --------
def lista_operaciones(request):
    operaciones = Operacion.objects.select_related('usuario').all()
    return render(request, 'wallet/lista_operaciones.html', {'operaciones': operaciones})

def crear_operacion(request):
    form = OperacionForm(request.POST or None)

    if form.is_valid():
        operacion = form.save()

        # lógica de negocio
        if operacion.tipo == 'DEP':
            operacion.usuario.saldo += operacion.monto
        else:
            operacion.usuario.saldo -= operacion.monto

        operacion.usuario.save()

        return redirect('lista_operaciones')

    return render(request, 'wallet/form_operacion.html', {'form': form})