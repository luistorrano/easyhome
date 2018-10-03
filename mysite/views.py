from django.shortcuts import render
from .forms import *
from .models import Republica, Usuario
from .utils import encontrar_republica
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required

def index(request):
    import pdb; pdb.set_trace()
    form = LatLngForm()
    return render(request,'index.html', {'form':form})

@csrf_exempt
def estudante(request):
    import pdb; pdb.set_trace()

    filename = '/home/luis/easyhome/mysite/static/json/pontos.json'
    if request.POST:
        if request.POST.get('latitude') != "":    
            republicas = encontrar_republica(request.POST.get('latitude'),request.POST.get('longitude'))
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
        else:
            return redirect('index')
 
        return render(request,'estudante.html', {'republicas':republicas})
    else:
        return redirect('index')
@login_required(login_url='/login/')
def cadastro_republica(request):
    form = republicaForm()
    if request.POST:
        form = republicaForm(request.POST)
        if form.is_valid():
            rep = form.save(commit=False)
            rep.user = request.user
            rep.save()
            import pdb ; pdb.set_trace()    
            return redirect('minhas-republicas')
    return render(request,'cadastro_republica.html',{'form':form })

def cadastro_usuario(request):
    form = CustomUserCreationForm()
    if request.POST:
        form = CustomUserCreationForm(request.POST)
        import pdb ; pdb.set_trace()
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request,user)
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

@login_required(login_url='/login/')
def excluir_conta(request):
    user = Usuario.objects.get(username=request.user.username)
    user.delete()
    return redirect('index')
    
@login_required(login_url='/login/')
def minhas_republicas(request):
    import pdb; pdb.set_trace()
    if request.user.tipo_acesso == 'P':
        republicas = Republica.objects.filter(user=request.user)
    else:
        return redirect('index')
    return render(request,'minhas_republicas.html',{'republicas':republicas})
    
def loginUsuario(request):
    import pdb ; pdb.set_trace()
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('perfil')
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password1'])
        login(request,user)
        return redirect('perfil')
    return render(request,'login.html')

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
    import pdb; pdb.set_trace()
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
    return redirect('minhas-republicas')
    
@login_required(login_url='/login/')
def mensagens_republica(request,republica_id):
    republica = Republica.objects.filter(id=republica_id)
    form = msgFormUsuario()
    if request.POST:
        import pdb; pdb.set_trace()
        json_data = {"mensagens":{ "mensagem" : [request.POST.get('mensagem')], "usuario":[request.user.username]}}
        
        
    return render(request,'mensagens_republica.html',{"form":form })

def tirar_duvidas(request, republica_id):
    usuario = Usuario.objects.filter(id=request.user.id)
    form = msgForm()
    republica = Republica.objects.filter(id=republica_id)
    republica = republica[0]
    mensagem = republica.mensagem
    import pdb; pdb.set_trace()    
    if request.method == "POST" and request.user.tipo_acesso == "E":
        json_data = { "mensagem" : [request.POST.get('mensagem')], "usuario":[request.user.username]}
        mensagens_exibidas = []
        for msg in mensagem['mensagens']:
            if msg['usuario'][0] == request.user.username:
                mensagens_exibidas.append(msg['mensagem'])
        msg_enviada = [request.POST.get('mensagem')]
        mensagens_exibidas.append(msg_enviada)
        mensagem['mensagens'].append(json_data)
        republica.mensagem = mensagem
        republica.save()
        mensagem = mensagens_exibidas
    
    
    return render(request,'tirar_duvidas.html',{'form': form, 'republica_id':republica_id , 'mensagens_existentes':mensagem})
        