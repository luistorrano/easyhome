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
from django.urls import path, include, re_path
from mysite.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('estudante/', estudante, name='estudante'),
    path('cadastrar-republica/', cadastro_republica, name='cadastrar-republica'),
    path('cadastrar-usuario/', cadastro_usuario, name='cadastrar-usuario'),
    path('perfil/', perfil, name='perfil'),
    path('alterar-usuario/', alterar_usuario, name='alterar-usuario'),
    path('excluir-conta/', excluir_conta, name='excluir-conta'),
    path('minhas-republicas/', minhas_republicas, name='minhas-republicas'),
    path('login/', loginUsuario, name='login'),
    path('logout/', logoutUsuario, name='logout'),
    re_path('perfil-republica/(?P<republica_id>\d+)/$', perfil_republica, name='perfil-republica'),
    re_path('excluir-republica/(?P<republica_id>\d+)/$', excluir_republica, name='excluir-republica'),
    re_path('alterar-republica/(?P<republica_id>\d+)/$', alterar_republica, name='alterar-republica'),
    re_path('mensagens-republica/(?P<republica_id>\d+)/$', mensagens_republica, name='mensagens-republica'),
    path('busca/', busca, name='busca'),
    re_path('tirar-duvidas/(?P<republica_id>[0-9])/$', tirar_duvidas, name='tirar-duvidas')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


