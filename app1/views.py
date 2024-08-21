
from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render


class ProductoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



def lista_productos(request):
    return render(request, 'productos.html')


'''
def agregar_producto(request):
    return render(request, 'agregar_producto.html')
'''
# app1/views.py

from django.shortcuts import render, redirect
from .models import Producto

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        codigo = request.POST.get('codigo')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        tipo = request.POST.get('tipo')

        # Verifica que todos los campos se están capturando correctamente
        print(nombre, codigo, descripcion, precio, tipo)

        # Guardar el nuevo producto en la base de datos
        Producto.objects.create(
            nombre=nombre,
            codigo=codigo,
            descripcion=descripcion,
            precio=precio,
            tipo=tipo
        )
        return redirect('producto_list')  # Redirige a la lista de productos después de guardar

    return render(request, 'agregar_producto.html')
