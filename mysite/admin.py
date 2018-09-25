from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Republica, Usuario

class RepublicaAdmin(admin.ModelAdmin):
    list_display = ['nome','endereco','bairro','qtd_vagas','tipo_imovel','data_registro']
    search_fields = ['nome','endereco','estado','bairro','qtd_vagas','tipo_imovel','data_registro']
    prepopulated_fields = {'slug':('endereco',)}

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['endereco','estado','telefone','rg','cpf','genero','tipo_acesso','email','data_registro']
    search_fields = ['endereco','estado','telefone','rg','cpf']


admin.site.register(Republica, RepublicaAdmin)
admin.site.register(Usuario,UsuarioAdmin)