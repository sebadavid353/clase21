from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name="index"),
    path('producto_categoria_list/',views.producto_categoria_list, name="producto_categoria_list"),
    path('producto_categoria_create/',views.Producto_categoria_create, name="producto_categoria_create"),
    
]