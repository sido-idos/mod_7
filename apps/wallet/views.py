from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Operacion
from .forms import UsuarioForm, OperacionForm

# Create your views here.

def lista_usuarios(request):
    nombre = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'wallet/lista_usuarios.html', {'usuarios': usuarios, 'nombre': nombre})

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

def lista_operaciones(request):
    usuario_q = ''
    tipo_q = ''
    operaciones = Operacion.objects.all()

    if request.method == 'POST':
        usuario_q = request.POST.get('usuario', '').strip()
        tipo_q = request.POST.get('tipo', '').strip()

        if usuario_q:
            operaciones = operaciones.filter(usuario__nombre__icontains=usuario_q)
        if tipo_q:
            operaciones = operaciones.filter(tipo__icontains=tipo_q)

    return render(request, 'wallet/lista_operaciones.html', {
        'operaciones': operaciones,
        'usuario_q': usuario_q,
        'tipo_q': tipo_q
    })

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