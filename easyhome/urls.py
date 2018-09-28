"""easyhome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from mysite.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('estudante/', estudante, name='estudante'),
    path('cadastrar-republica/', cadastro_republica, name='cadastrar-republica'),
    path('cadastrar-usuario/', cadastro_usuario, name='cadastrar-usuario'),
    path('perfil/', perfil, name='perfil'),
    path('alterar-usuario/', alterar_usuario, name='alterar-usuario'),
    path('excluir-conta/', excluir_conta, name='excluir-conta'),

]
