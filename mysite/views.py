from django.shortcuts import render
from .forms import LatLngForm, republicaForm, CustomUserCreationForm, CustomUserChangeForm
from .models import Republica, Usuario
from .utils import encontrar_republica
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import json
from decimal import Decimal

def index(request):
    form = LatLngForm()
    return render(request,'index.html', {'form':form})

@csrf_exempt
def estudante(request):
    filename = '/home/luis/easyhome/mysite/static/json/pontos.json'

    if request.POST:
        if request.POST.get('latitude'):    
            republicas = encontrar_republica(Decimal(float(request.POST.get('latitude'))),Decimal(float(request.POST.get('longitude'))))
            if republicas:
                arq = open(filename,'w+')
                latlng = []
                for republica in republicas:
                    latlng.append({
                        "Latitude": str(republica.latitude),
                        "Longitude": str(republica.longitude)
                    })
                latlng = str(latlng)
                latlng = latlng.replace("'",'"')
                arq.write(latlng)
                arq.close()
    return render(request,'estudante.html', {'republicas':republicas})

def cadastro_republica(request):
    form = republicaForm()
    if request.POST:
        form = republicaForm(request.POST)
        if form.is_valid():
            form.save()
            #retornar para pagina de minhas republicas
    return render(request,'cadastro_republica.html',{'form':form })

def cadastro_usuario(request):
    form = CustomUserCreationForm()
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'cadastro_usuario.html',{'form':form})

def perfil(request):
    perfil = Usuario.objects.filter(username=request.user.username)
    return render(request,'perfil.html',{'perfil':perfil})

def alterar_usuario(request):
    if request.POST:
        user = Usuario.objects.get(username=request.POST.get('username'))
        user.email = request.POST.get('email')
        user.nome = request.POST.get('nome')
        user.endereco = request.POST.get('endereco')
        user.genero = request.POST.get('genero')
        user.estado = request.POST.get('estado')
        user.cidade = request.POST.get('cidade')
        user.telefone = request.POST.get('telefone')
        user.rg = request.POST.get('rg')
        user.cpf = request.POST.get('cpf')
        user.save()
    user = Usuario.objects.filter(username=request.user.username)
    estado = CustomUserCreationForm()
    form = user[0]
    return render(request,'alterar_usuario.html',{'form':form,'estado':estado})

def excluir_conta(request):
    import pdb; pdb.set_trace()
    user = Usuario.objects.get(username=request.user.username)
    user.delete()
    return redirect('index')
    
    