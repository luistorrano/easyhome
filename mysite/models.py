from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from geoposition.fields import GeopositionField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.conf import settings
from jsonfield import JSONField
import json
class Usuario(AbstractUser):
    ##todo__ incluir data de nascimento
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    )
    ACESSOS = (
        ('P', 'Proprietario'),
        ('E', 'Estudante'),
    )
    nome = models.CharField(
        max_length=255,
        verbose_name=u'Nome',
        help_text='Digite o seu nome'
        )
    endereco = models.CharField(
        max_length=255,
        verbose_name=u'Endereço',
        help_text='Para uma melhor localização no mapa, \
        preencha sem abreviações. \
        Ex: Rua taquari,  100'
        )
    mensagem = JSONField(
        null=True, blank=True
    )
    telefone = models.CharField(
        'Telefone',
        max_length=15
        )
    rg = models.CharField(
        'RG',
        max_length=11,
        blank=False,
        null=False
        )
    cpf = models.CharField(
        'CPF',
        max_length=14,
        blank=False,
        null=False
        )
    genero = models.CharField(
        'Gênero',
        max_length=1,
        choices=GENEROS
        )
    tipo_acesso = models.CharField(
        'Tipo de acesso',
        max_length=1,
        choices=ACESSOS,
        blank=False,
        null=False
        )
    imagem = models.ImageField(
        'Fotos',
        upload_to='imagens/',
        blank=True,
        null=True
        )
    data_registro = models.DateField(
        'Registrado em',
        auto_now_add=True
        )
    email = models.EmailField(
        max_length=254,
        unique=True
        )
    

    def __str__(self):
    
        return self.email

class Republica(models.Model):
    
    GENEROS_REPUBLICA = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('A', 'Ambos')
    )
    nome = models.CharField(
        'Nome',
        max_length=200,
        blank=True,
        null=False
        )
    email = models.EmailField(
        max_length=254
        )
    endereco = models.CharField(
        max_length=255,
        verbose_name=u'Endereço',
        help_text='Para uma melhor localização no mapa, \
        preencha sem abreviações. \
        Ex: Rua taquari,  100'
        )
    slug = models.SlugField(
        'Atalho'
        )
    genero = models.CharField(
        'Gênero',
        max_length=1,
        choices=GENEROS_REPUBLICA
        )
    qtd_vagas = models.PositiveIntegerField(
        'Quantidade de vagas',
        default=1,
        validators=[MinValueValidator(1)]
        )
    tipo_imovel = models.CharField(
        'tipo de imóvel',
        max_length=20,
        null=False,
        blank=False
        )
    imagens = models.FileField(
        'Fotos',
        upload_to='media/imagens/'
        )
    data_registro = models.DateField(
        'Registrado em',
        auto_now_add=True
        )

    latitude = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        default=33
        )
    longitude = models.DecimalField(
        max_digits=30,
        decimal_places=20,
        default=33
        )
    valor = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    comentarios = models.CharField(
        max_length=1000,
        null=True, 
        blank=True,
    )   
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        default=1,
        on_delete=models.CASCADE    
    )
    mensagem = JSONField(
        null=True, blank=True
    )
    rep_id = models.IntegerField(
        null=True,
        blank=True
    )
    def __str__(self):
    
        return self.nome

    class Meta:
        verbose_name = 'República'
        verbose_name_plural = 'Repúblicas'


class Mensagem(models.Model):
    republica = models.ForeignKey(Republica, related_name='mensagem_republica', on_delete=models.CASCADE)
    pergunta = models.TextField("Pergunta")
    pergunta_datetime = models.DateTimeField("Quando foi realizada a Pergunta", auto_now_add=True)
    usuario_pergunta = models.ForeignKey(Usuario, related_name='mensagem_usuario', on_delete=models.CASCADE)
    resposta = models.TextField("Resposta Proprietario", blank=True, null=True)
    resposta_datetime = models.DateTimeField("Quando foi Respondido", blank=True, null=True)

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return str(self.id)

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename) 

class ImagensRepublica(models.Model):
    republica = models.ForeignKey(Republica, related_name='imagem_republica', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')