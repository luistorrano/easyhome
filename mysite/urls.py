from django.urls import path,re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('^$', 'index', views.index),
    path('estudante/', views.estudante),
    path('cadastrar-republica/', views.cadastro_republica),
    path('cadastrar-usuario/', views.cadastro_usuario),
    path('perfil/', views.perfil),
    path('alterar-usuario/', views.alterar_usuario),
    path('excluir-conta/', views.excluir_conta),
    path('minhas-republicas/', views.minhas_republicas),
    path('login/', views.loginUsuario),
    path('logout/', views.logoutUsuario),
    path('mensagens-republica/<int:republica_id>/<int:pergunta_id>/', views.mensagens_republica, name='mensagens_republica')
    re_path('perfil-republica/(?P<republica_id>[0-9])/$', views.perfil_republica),
    re_path('excluir-republica/(?P<republica_id>[0-9])/$', views.excluir_republica),
    re_path('alterar-republica/(?P<republica_id>[0-9])/$', views.alterar_republica),
    #re_path('mensagens-republica/(?P<republica_id>[0-9])/(?P<pergunta_id>[0-9])/$', mysite.views.mensagens_republica, name="mensagens_republica"), 
    #re_path('mensagens-republica/(?P<republica_id>[0-9])/$', mysite.views.mensagens_republica, name="mensagens_republica"),
    path('busca/', views.busca),
    re_path('tirar-duvidas/(?P<republica_id>[0-9])/$', views.tirar_duvidas, name='tirar-duvidas')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)