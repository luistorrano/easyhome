from django.contrib import admin
from .models import Republica, Usuario

class RepublicaAdmin(admin.ModelAdmin):
    list_display = ['nome','endereco','bairro','qtd_vagas','tipo_imovel','data_registro']
    search_fields = ['nome','endereco','bairro','qtd_vagas','tipo_imovel','data_registro']
    prepopulated_fields = {'slug':('endereco',)}
admin.site.register(Republica, RepublicaAdmin)
admin.site.register(Usuario)