from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from geoposition.fields import GeopositionField
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Usuario(AbstractUser):
    
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    )
    ACESSOS = (
        ('P', 'Proprietario'),
        ('E', 'Estudante'),
    )
    endereco = models.CharField(
        max_length=255,
        verbose_name=u'Endereço',
        help_text='Para uma melhor localização no mapa, \
        preencha sem abreviações. \
        Ex: Rua taquari,  100'
        )
    mensagem = models.CharField(
        max_length=10000,
        verbose_name='Mensagem',
        help_text='Digite uma mensagem'
        )
    cidade_estudante = models.CharField(
        max_length=255,
        default='sp',
        null=True,
        blank=True,
        help_text="Para uma melhor localização no mapa, \
        preencha sem abreviações. Ex: Belo Horizonte"
        )
    estado = models.CharField(
        max_length=2,
        null=True, 
        blank=True,
        choices=STATE_CHOICES
        )
    latitude = models.DecimalField(
        max_digits=30,
        decimal_places=28
        )
    longitude = models.DecimalField(
        max_digits=30,
        decimal_places=28
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
    bairro = models.CharField(
        'Bairro',
        max_length=200,
        blank=True,
        )
    genero = models.CharField(
        'Gênero',
        max_length=1,
        choices=GENEROS_REPUBLICA
        )
    qtd_vagas = models.IntegerField(
        'Quantidade de vagas'
        )
    tipo_imovel = models.CharField(
        'tipo de imóvel',
        max_length=20,
        null=False,
        blank=False
        )
    imagens = models.ImageField(
        'Fotos',
        upload_to='imagens/'
        )
    data_registro = models.DateField(
        'Registrado em',
        auto_now_add=True
        )

    estado = models.CharField(
        max_length=2,
        null=True, 
        blank=True,
        choices=STATE_CHOICES
        )
    latitude = models.DecimalField(
        max_digits=30,
        decimal_places=28
        )
    longitude = models.DecimalField(
        max_digits=30,
        decimal_places=28
        )
    def __str__(self):
    
        return self.nome

    class Meta:
        verbose_name = 'República'
        verbose_name_plural = 'Repúblicas'