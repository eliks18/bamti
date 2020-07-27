from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from . import forms
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# @login_required(login_url='login/', redirect_field_name='')
def welcome(request):
    # Si estamos identificados devolvemos la portada
    # if request.user.is_authenticated:
    #     return render(request, "users/welcome.html")
    # # En otro caso redireccionamos al login
    # return redirect('/login')
    return render(request, "users/welcome.html")

def register(request):
    return render(request, "users/register.html")

def login(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return redirect('/')
    
    # Creamos el formulario de autenticación vacío
    form = forms.LoginForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = forms.LoginForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')