from django.shortcuts import render
from .forms import *
from .models import Republica, Usuario, Mensagem, ImagensRepublica
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
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from channels.layers import get_channel_layer
from easyhome.settings import BASE_DIR
from django.urls import reverse


def index(request):

    form = LatLngForm()
    return render(request,'index.html', {'form':form})

@csrf_exempt
def estudante(request):
    #import ipdb; ipdb.set_trace()
    filename = BASE_DIR + '/mysite/static/json/pontos.json'
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
    form = republicaForm()
    if request.POST:
        files = request.FILES
        form = republicaForm(request.POST,files)
        if form.is_valid():
            rep = form.save(commit=False)
            '''
            cidade = request.POST.get('cidade').lower()
            cidade = normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('ASCII')
            rep.cidade = cidade
            '''                
            rep.user = request.user
            rep.save()
            
            for i in request.FILES.getlist('imagens'):
                imagem = ImagensRepublica(republica=rep, image=i)
                imagem.save()
            return redirect('minhas-republicas')
        else:
            if 'latitude' in form.errors:
                form.errors['endereco'] = ["Digite um endereço válido e selecione na lista de endereços."]
                form.errors.pop('latitude')
                form.errors.pop('longitude')
                print (form.errors)
            return render(request,'cadastro_republica.html', {'errors': form.errors})
            
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
        else:
            return render(request,'cadastro_usuario.html', {'errors': form.errors})
    return render(request,'cadastro_usuario.html',{'form':form})

@login_required
def perfil(request):
    perfil = Usuario.objects.filter(username=request.user.username)
    return render(request,'perfil.html',{'perfil':perfil})

@login_required(login_url='/login/')
def alterar_usuario(request):
    if request.POST:
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
    import ipdb; ipdb.set_trace()
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
    if request.method == "POST":
        uri = request.get_raw_uri()
        uri = uri.split('/')
        uri = uri[4]
        alterar = alterar_republica(request, uri)
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
    ##todo__ fazer a alteração dos dados da república.
    ##todo__ fazer o sistema reconhecer dados inválidos.
    rep = Republica.objects.get(id=republica_id)
    rep.nome = request.POST['nome']
    rep.email = request.POST['email']
    rep.endereco = request.POST['endereco']
    gen = request.POST['genero']
    if gen == "Masculino":
        gen = "M"
    elif gen == "Feminino":
        gen = "F"
    else:
        gen = "A"
    rep.genero = gen
    rep.qtd_vagas = request.POST['qtd_vagas']
    rep.tipo_imovel = request.POST['id_tipo_imovel']
    valor = request.POST['valor']
    valor = valor.split(',')
    valor = valor[0]
    rep.valor = valor
    rep.save()
    return ''#redirect('minhas-republicas')
    
@login_required(login_url='/login/')
def mensagens_republica(request,republica_id, pergunta_id=None):
    POST = request.POST
    republica = Republica.objects.get(id=republica_id)
    mensagens = Mensagem.objects.filter(republica=republica).order_by('pergunta_datetime')
    usuario = request.user
    #import ipdb; ipdb.set_trace()
    if POST:
        if usuario.tipo_acesso == 'E':
            mensagem = Mensagem(
                                republica = republica,
                                pergunta = POST['mensagem'],
                                usuario_pergunta = usuario
                                )
            mensagem.save()
        elif usuario.tipo_acesso == 'P':
            mensagem = Mensagem.objects.get(id=pergunta_id)
            mensagem.resposta = POST['mensagem']
            mensagem.resposta_datetime = datetime.now()
            mensagem.save()

        
        return redirect(reverse('mensagens-republica', kwargs={'republica_id':republica_id}))
                
    
    context = {
        'mensagens': mensagens,
        'republica': republica
    }
  
    return render(request,'mensagens_republica.html', context)

def tirar_duvidas(request, republica_id):
    ChatConsumer.connect()
    #form = msgForm()   
    #republica = Republica.objects.filter(id=republica_id)
    #republica = republica[0]
    #msage = republica.mensagem
    #mensagem = republica.mensagem
    #json_data = {}
    #if request.POST:
    #    if republica.mensagem:
    #        for msg in republica.mensagem['mensagens']:
    #            if msg['usuario'][0] == request.user.username and msg['tipo_mensagem'][0] == 'user_to_rep':
    #                msg['mensagem'].append(request.POST.get('mensagem'))
    #                republica.save()
    #                json_data = {}
    #                break
    #            else:    
    #                json_data = { "mensagem" : [request.POST.get('mensagem')], "usuario":[request.user.username], "republica":[republica_id], "nome_republica":[republica.nome], "tipo_mensagem": "user_to_rep","data":[datetime.now()]}
    #    else:
    #        json_data = { "mensagem" : [request.POST.get('mensagem')], "usuario":[request.user.username], "republica":[republica_id], "nome_republica":[republica.nome], "tipo_mensagem": "user_to_rep","data":[datetime.now()]}
    #    if json_data != {}:
    #        try:
    #            republica.mensagem['mensagens'].append(json_data)
    #        except Exception:
    #            republica.mensagem = {'mensagens':[json_data]}
    #        republica.save()
    #mensagens = []
    #if mensagem:
    #    for msg in mensagem['mensagens']:
    #        if msg['usuario'][0] == request.user.username:
    #            mensagens.append(msg)
    
    return render(request,'tirar_duvidas.html',{'room_name_json':republica_id})

def busca(request):
    ##todo__retornar msg de erro qd campos faltarem.
    ##todo__ verificar validação dos campos
    ##todo__ tirar obrigatoriedade do campo endereço (ajustar a logica para trazer todas as repúblicas caso não haja edereço, e então filtrar pelos outros campos.)
    form = formFiltros()
    if request.POST:
        republicas = busca_filtros(request.POST.get('latitude'), request.POST.get('longitude'),request.POST.get('qtd_vagas'),request.POST.get('tipo_imovel'), request.POST.get('genero'),request.POST.get('valor').replace("R$ ",""))
        return render(request,'resultados_busca.html', {'republicas':republicas})
    return render(request,'busca_filtros.html',{'form':form,'range':range(5000)})

class ChatConsumer(WebsocketConsumer):
    def connect(self, user, republica):
        self.room_name = str(user.username)+str(republica)#self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'tirar-duvidas_%s' % self.room_name
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
    
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
