from django.shortcuts import render

from . import forms

# Create your views here.

   

def index(request):
    return render(request, "home/index.html",)




from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm


def login_request(request):
    if request.method == "POST":    
        form = AuthenticationForm(request.POST, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home/index.html", {'mensaje':f"Bienvenido {usuario}"})
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {'form':form})



#registro basado en funciones
    
def register(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request, "home/index.html", {"mensaje":'Usuario Creado'})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html",{"form":form})
