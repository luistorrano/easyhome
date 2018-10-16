from django.shortcuts import render
from .forms import *
from .models import Republica, Usuario
from .utils import encontrar_republica, busca_filtros
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import  RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
import geopy.distance
from datetime import datetime
from unicodedata import normalize


def index(request):

    form = LatLngForm()
    return render(request,'index.html', {'form':form})

@csrf_exempt
def estudante(request):

    filename = '/home/luis/easyhome/mysite/static/json/pontos.json'
    if request.POST:
        if request.POST.get('latitude') != "":    
            republicas = encontrar_republica(request.POST.get('latitude'),request.POST.get('longitude'))
            arq = open(filename,'w+')
            latlng = []
            for republica in republicas:
                rep = (republica.latitude,republica.longitude)
                usuario = (request.POST.get('latitude'),request.POST.get('longitude'))
                distancia = geopy.distance.vincenty(rep,usuario).km
                distancia = round(distancia,2)
                latlng.append({
                    "Latitude": str(republica.latitude),
                    "Longitude": str(republica.longitude),
                    "Nome":str(republica.nome),
                    "vagas":str(republica.qtd_vagas),
                    "genero_aceito":str(republica.genero),
                    "tipo_imovel":str(republica.tipo_imovel),
                    "distancia":str(distancia)
                })
            latlng = str(latlng)
            latlng = latlng.replace("'",'"')
            arq.write(latlng)
            arq.close()
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
        else:
            return redirect('index')
 
        return render(request,'estudante.html', {'republicas':republicas, 'latitude':latitude,'longitude':longitude})
    else:
        return redirect('index')
@login_required(login_url='/login/')
def cadastro_republica(request):
    import pdb; pdb.set_trace()
    form = republicaForm()
    if request.POST:
        files = request.FILES.getlist('imagens')
        form = republicaForm(request.POST,files)
        if form.is_valid():
            rep = form.save(commit=False)
            cidade = request.POST.get('cidade').lower()
            cidade = normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('ASCII')
            rep.cidade = cidade
            rep.user = request.user
            rep.save()
            return redirect('minhas-republicas')
    return render(request,'cadastro_republica.html',{'form':form })

def cadastro_usuario(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    form = CustomUserCreationForm()
    if request.POST:
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request,user)
            return redirect('index')
    return render(request,'cadastro_usuario.html',{'form':form})

@login_required
def perfil(request):
    import pdb; pdb.set_trace()
    perfil = Usuario.objects.filter(username=request.user.username)
    return render(request,'perfil.html',{'perfil':perfil})

@login_required(login_url='/login/')
def alterar_usuario(request):
    ##todo__verificar pq não está alterando gênero na alteração de usuário
    if request.POST:
        import pdb; pdb.set_trace()
        user = Usuario.objects.get(username=request.POST.get('username'))
        user.email = request.POST.get('email')
        user.nome = request.POST.get('nome')
        user.endereco = request.POST.get('endereco')
        user.genero = request.POST.get('genero')
        user.telefone = request.POST.get('telefone')
        user.rg = request.POST.get('rg')
        user.cpf = request.POST.get('cpf')
        user.save()
        return redirect('perfil')
    user = Usuario.objects.filter(username=request.user.username)
    estado = CustomUserCreationForm()
    form = user[0]
    return render(request,'alterar_usuario.html',{'form':form,'estado':estado})

@login_required(login_url='/login/')
def excluir_conta(request):

    user = Usuario.objects.get(username=request.user.username)
    user.delete()
    return redirect('index')
    
@login_required(login_url='/login/')
def minhas_republicas(request):

    if request.user.tipo_acesso == 'P':
        republicas = Republica.objects.filter(user=request.user)
    else:
        return redirect('index')
    return render(request,'minhas_republicas.html',{'republicas':republicas})
    
def loginUsuario(request):

    errors = ''
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('perfil')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        if user is not None:
            login(request,user)
            return redirect('perfil')
        else:
            return render(request,'login.html', {'errors': 'Usuário ou senha inválidos'})
    context = {'errors:':errors}
    return render(request,'login.html',context,RequestContext(request))


@login_required(login_url='/login/')
def logoutUsuario(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
            return redirect('index')
        else:
            return redirect('login')

@login_required(login_url='/login/')
def perfil_republica(request,republica_id):
    perfil = Republica.objects.filter(id=republica_id)
    if request.user.tipo_acesso == "E":
        
        form = msgFormUsuario()
        return render(request,'perfil_republica.html',{'perfil':perfil, 'acesso':request.user.tipo_acesso, 'form':form})
    else:
        return render(request,'perfil_republica.html',{'perfil':perfil, 'acesso':request.user.tipo_acesso})

@login_required(login_url='/login/')
def excluir_republica(request,republica_id):

    rep = Republica.objects.filter(id=republica_id)
    rep = rep[0]
    if rep:
        if request.user == rep.user:
            rep.delete()
    return redirect('minhas-republicas')

@login_required(login_url='/login/')
def alterar_republica(request,republica_id):
    import pdb; pdb.set_trace()
    ##todo__ fazer a alteração dos dados da república.
    ##todo__ fazer o sistema reconhecer dados inválidos.
    return redirect('minhas-republicas')
    
@login_required(login_url='/login/')
def mensagens_republica(request,republica_id):

    republica = Republica.objects.filter(id=republica_id)
    republica = republica[0]
    form = msgFormUsuario()
    if request.POST:
        for msg in republica.mensagem['mensagens']:
            if msg['republica'][0] == request.user.username:
                msg['mensagem'].append(request.POST.get('mensagem'))
                republica.save()
                json_data = {}
                break
            else:
                json_data = { "mensagem" : [request.POST.get('mensagem')], "origem":[request.user.username], "republica":[republica_id], "nome_republica":[republica.nome], "tipo_mensagem":"rep_to_user","data":[datetime.now()]}
        if json_data != {}:
            republica.mensagem['mensagens'].append(json_data)
        republica.save()
                
    rep = Republica.objects.filter(id=republica_id)
    rep = rep[0]
    mensagens = rep.mensagem['mensagens']
    return render(request,'mensagens_republica.html',{"form":form, "mensagens" : mensagens})

def tirar_duvidas(request, republica_id):

    form = msgForm()
    republica = Republica.objects.filter(id=republica_id)
    republica = republica[0]
    msage = republica.mensagem
    mensagem = republica.mensagem
    json_data = {}
    if request.POST:
        for msg in republica.mensagem['mensagens']:
            if msg['usuario'][0] == request.user.username and msg['tipo_mensagem'][0] == 'user_to_rep':
                msg['mensagem'].append(request.POST.get('mensagem'))
                republica.save()
                json_data = {}
                break
            else:    
                json_data = { "mensagem" : [request.POST.get('mensagem')], "usuario":[request.user.username], "republica":[republica_id], "nome_republica":[republica.nome], "tipo_mensagem": "user_to_rep","data":[datetime.now()]}
        if json_data != {}:
            republica.mensagem['mensagens'].append(json_data)
            republica.save()
    mensagens = []
    for msg in mensagem['mensagens']:
        if msg['usuario'][0] == request.user.username:
            mensagens.append(msg)
    
    mensagens = {'mensagens':mensagens}
    return render(request,'tirar_duvidas.html',{'form': form, 'republica_id':republica_id , 'mensagens_existentes':mensagens})

def busca(request):
    ##todo__retornar msg de erro qd campos faltarem.
    ##todo__ verificar validação dos campos
    ##todo__ tirar obrigatoriedade do campo endereço (ajustar a logica para trazer todas as repúblicas caso não haja edereço, e então filtrar pelos outros campos.)
    form = formFiltros()
    if request.POST:
        republicas = busca_filtros(request.POST.get('latitude'), request.POST.get('longitude'),request.POST.get('qtd_vagas'),request.POST.get('tipo_imovel'), request.POST.get('genero'),request.POST.get('valor').replace("R$ ",""))
        return render(request,'resultados_busca.html', {'republicas':republicas})
    return render(request,'busca_filtros.html',{'form':form,'range':range(5000)})
