from decimal import Decimal
from mysite.models import Republica, Usuario
PRECISION_MAP = {
    0: Decimal('1.0'),      # -/+ 111  km
    1: Decimal('0.1'),      # -/+ 11.1 km
    2: Decimal('0.01'),     # -/+ 1.11 km
    3: Decimal('0.001'),    # -/+ 111  m
    4: Decimal('0.0001'),   # -/+ 11.1 m
    5: Decimal('0.00001'),  # -/+ 1.11 m
    6: Decimal('0.000001'), # -/+ 11.1 cm
    7: Decimal('11.0'), 
}


def encontrar_republica(lat, lng):
    precison = 1
    _range = PRECISION_MAP[precison]
    lat = Decimal(lat)
    lng = Decimal(lng)
    #https://gist.github.com/chronossc/a67517621c2a9d4c2f14
    republicas = Republica.objects.filter(
        latitude__gte= lat - (_range ), latitude__lte=lat + (_range ),
        longitude__gte=lng - (_range ), longitude__lte=lng + (_range)
    )
    
    return republicas
def busca_filtros(latitude, longitude, qtd_vagas, tipo_imovel, genero, valor):
    valor = valor.replace(',','.')
    valor = Decimal(valor)
    republicas = []
    precison = 1
    _range = PRECISION_MAP[precison]
    lat = Decimal(latitude)
    lng = Decimal(longitude)
    
    rep = Republica.objects.filter(
        latitude__gte=lat - (_range ), latitude__lte=lat + (_range ),
        longitude__gte=lng - (_range ), longitude__lte=lng + (_range)
    )
    if rep:
        rep_tipo_imovel = rep.filter(tipo_imovel=tipo_imovel)
        if rep_tipo_imovel:
            rep_vagas = rep_tipo_imovel.filter(qtd_vagas__gte=qtd_vagas)
            rep = rep_vagas
            if rep_vagas:
                rep_valor = rep_vagas.filter(valor__lte=valor)
                rep = rep_valor
                if rep_valor:
                    rep_genero = rep_valor.filter(genero=genero)
                    rep = rep_genero
                else:
                    rep = rep_vagas
            else:
                rep = rep_vagas
        else:
            rep = rep

    return rep
#def enviar_mensagem(mensagem):

