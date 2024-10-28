from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("pagina_inicio"))
        else:
            return render(request, "usuario/login.html", {"msj": "Credenciales incorrectas"})
    return render(request, "usuario/login.html")


def logout_view(request):
    logout(request)
    return render(request, "usuario/login.html", {"msj": "Deslogueado"})



@login_required(login_url='usuario:login')
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/listar_usuarios.html', {'usuarios': usuarios})


#@login_required
"""def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/crear_usuario.html', {'form': form})

#@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar_usuario.html', {'form': form})

#@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')
"""