# app1/urls.py

from django.urls import path
from .views import ProductoListCreateAPIView, agregar_producto, lista_productos

urlpatterns = [
    path('productos/', ProductoListCreateAPIView.as_view(), name='producto_list-create'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('productos/', lista_productos, name='producto_list'),

]
