# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from localflavor.br.br_states import STATE_CHOICES
from .models import Usuario, Republica

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ('username','password1','password2','nome', 'email','endereco','telefone','rg', 'cpf','genero','tipo_acesso', 'imagem')
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['genero'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_acesso'].widget.attrs['class'] = 'form-control'



        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover form-control', 'placeholder':help_text, 'data-placement':'right', 'data-container':'body'})





class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('username', 'email','endereco','mensagem','telefone','rg', 'cpf','genero','tipo_acesso', 'imagem')
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['genero'].widget.attrs['class'] = 'form-control'
        self.fields['tipo_acesso'].widget.attrs['class'] = 'form-control'
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover form-control', 'placeholder':help_text, 'data-placement':'right', 'data-container':'body'})



class LatLngForm(forms.ModelForm):
    
    class Meta:
        model = Republica
        fields = ('latitude','longitude')

class republicaForm(forms.ModelForm):
    CHOICES = [
        ('CS','Casa'),
        ('AP','Apartamento')
        ]
    CHOICES_GENERO = [
        ('M','Masculino'),
        ('F','Feminino'),
        ('A','Ambos')
        ]
    nome = forms.CharField(
        max_length=254,
        help_text='Digite o nome da república'
        )
    email = forms.EmailField(
        max_length=254,
        required=False
        )
    endereco = forms.CharField(
        max_length=254,
        help_text= 'Ex: Rua Taquari, 44 - Mooca'
        )
    tipo_imovel = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect()
        )
    genero = forms.ChoiceField(
        choices=CHOICES_GENERO,
        )
    qtd_vagas = forms.IntegerField(
        help_text='Quantidade total de vagas'
        )
    valor = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        help_text='Valor Mensal'
        )
    class Meta:
        model = Republica
        fields = ('nome','endereco','email','qtd_vagas','tipo_imovel','latitude','longitude','genero','imagens','valor')
    def __init__(self, *args, **kwargs):
        super(republicaForm, self).__init__(*args, **kwargs)
        self.fields['genero'].widget.attrs['class'] = 'form-control'
        self.fields['valor'].widget.attrs['class'] = 'form-control'


        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover form-control', 'placeholder':help_text, 'data-placement':'right', 'data-container':'body'})

class msgForm(forms.ModelForm):
    class Meta:
        model = Republica
        fields = ('mensagem','rep_id')

class msgFormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('mensagem',)

class formFiltros(forms.ModelForm):
    class Meta:
        model = Republica
        fields = ('endereco', 'qtd_vagas', 'tipo_imovel','latitude','longitude','genero','valor')
    def __init__(self, *args, **kwargs):
        super(formFiltros, self).__init__(*args, **kwargs)
        self.fields['genero'].widget.attrs['class'] = 'form-control'
        self.fields['valor'].widget.attrs['class'] = 'form-control'
        self.fields['valor'].widget.attrs['type'] = 'range'
        self.fields['valor'].widget.attrs['min'] = '1'
        self.fields['valor'].widget.attrs['max'] = '5000'

class formLogin(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username','password')
    def __init__(self, *args, **kwargs):
        super(formLogin, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})