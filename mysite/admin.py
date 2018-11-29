from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Republica, Usuario, Mensagem

class RepublicaAdmin(admin.ModelAdmin):
    list_display = ['nome','endereco','qtd_vagas','tipo_imovel','data_registro']
    search_fields = ['nome','endereco','qtd_vagas','tipo_imovel','data_registro']
    prepopulated_fields = {'slug':('endereco',)}
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.owner = request.user
        super().save_model(request, obj, form, change)




class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['endereco','telefone','rg','cpf','genero','tipo_acesso','email','data_registro']
    search_fields = ['endereco','telefone','rg','cpf']


admin.site.register(Republica, RepublicaAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Mensagem)