from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from . import forms,models
# Create your views here.





def index(request: HttpRequest)->HttpResponse:
    return render(request, "producto/index.html",)

#vistas basadas en clases
from django.views.generic.list import ListView #listar objetos
from django.views.generic.edit import CreateView, UpdateView,DeleteView

class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria  #le indico que modelo voy a utilizar
    template_name = "producto/producto_categoria_list.html" #nombre de la plantilla
    context_object_name = 'categorias'

#loginrequired/requiredmixin para evitar que alguien que no es del stadd pueda crear productos etc 
class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm  #que formulario se va a usar
    template_name = "producto/producto_categoria_create.html"
    success_url = reverse_lazy( "producto:index")   # reverse_lazy esper a que se ejecute la funcion para luego ir a la url

class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/producto_categoria_delete.html"
    success_url = reverse_lazy( "producto:index")



class ProductoCategoriaUpdate(UpdateView):

    model = models.ProductoCategoria

    form_class = forms.ProductoCategoriaForm
    template_name = "producto/producto_categoria_update.html"
    success_url = reverse_lazy('producto:producto_categoria_list')


