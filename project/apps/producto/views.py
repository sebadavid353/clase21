from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect,render
from . import forms,models
# Create your views here.





def index(request):
    return render(request, "producto/index.html",)


def producto_categoria_list(request):
    categorias = models.ProductoCategoria.objects.all()
    context = {'categorias': categorias}
    return render(request, "producto/producto_categoria_list.html", context)


def Producto_categoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect("producto:index")
    else:
        form = forms.ProductoCategoriaForm()
    return render(request, "producto/producto_categoria_create.html",{'form': form})

