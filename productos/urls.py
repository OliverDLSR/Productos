"""
URL configuration for productos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import ProductoListCreateAPIView

from app1.views import lista_productos

urlpatterns = [
    
 
    path('admin/', admin.site.urls),
    path('', ProductoListCreateAPIView.as_view(), name='producto_list'),
    path('api/', include('app1.urls')),
    path('productos/', include('app1.urls')),

    path('admin/', admin.site.urls),
    path('', lista_productos, name='producto_list'),  # Página principal
    path('api/', include('app1.urls')),
    path('productos/', lista_productos, name='producto_list')
    
    
]
