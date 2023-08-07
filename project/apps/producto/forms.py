from django import forms

from . views import models


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = '__all__'