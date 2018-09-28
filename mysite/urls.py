from django.urls import path
from . import views

urlpatterns = [
    path('^$', 'index', views.index),
    path('estudante/', views.estudante),
    path('cadastrar-republica/', views.cadastro_republica),
    path('cadastrar-usuario/', views.cadastro_usuario),
    path('perfil/', views.perfil),
    path('alterar-usuario/', views.alterar_usuario),
    path('excluir-conta/', views.excluir_conta),

]