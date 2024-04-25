from django.shortcuts import get_object_or_404, render, redirect
from .forms import UserRegisterForm, AgregarUsuarioAGrupo
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # pragma: no cover
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:  # pragma: no cover
        form = UserRegisterForm
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/usuarios/login/')


@login_required
@allowed_users(allowed_roles=['admin'])
def administrar_usuarios(request):
    users = User.objects.all()
    return render(request, 'administrar_usuarios.html', {'usuarios': users})


@login_required
@allowed_users(allowed_roles=['admin'])
def editar_usuario(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = AgregarUsuarioAGrupo(request.POST)
        if form.is_valid():
            form.save(user_profile)
            return redirect('/usuarios/administrar/')
    else:
        form = AgregarUsuarioAGrupo(
            initial={'groups': user_profile.groups.first()})

    return render(request, 'editar_usuario.html', {'form': form, 'user_profile': user_profile})
