from django.db import models

# Create your models here.

class Usuario(models.Model):
    
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
        'Nome',
        max_length=200,
        blank=False,
        null=False
    )
    endereco = models.CharField(
        'Endereço',
        max_length=400,
        blank=False,
        null=False
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
    email = models.EmailField(
        'E-mail',
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
    
        return self.nome

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
        'Endereço',
        max_length=200,
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

    def __str__(self):
    
        return self.nome

    class Meta:
        verbose_name = 'República'
        verbose_name_plural = 'Repúblicas'